"""Read the reference configuration and get that object's documentation."""
import logging
import re
from pathlib import Path
from typing import cast, Any, List, Mapping, Union

import yaml
from pytkdocs.cli import process_config


logger = logging.getLogger(__name__)
TITLE_LINE_RE = re.compile(r"!!!\s?(\w.*)")


def _get_root_config() -> Mapping[str, Union[str, Mapping[str, str]]]:
    fp = Path("pyhugodoc.yaml")
    logger.debug("Reading configuration file.")
    try:
        raw_config = yaml.load(fp.read_text(), yaml.Loader)
        base = {
            "site_dir": raw_config["site_dir"],
            "reference_dir": raw_config["reference_dir"],
        }

        if handler := raw_config.get("handlers"):
            base["handlers"] = handler

        return base
    except KeyError as e:
        raise ValueError(
            f"Invalid configuration file; missing required key: {e.args[0]}"
        )


USER_CONFIG = _get_root_config()


def _get_objects_from_file(fp: Path) -> List[Mapping[str, Any]]:
    """
    Read a file from the user-defined _references directory, and get the objects
    defined in it.
    """
    logger.debug(f"Reading objects from file: {fp}")
    objects = []
    for obj in fp.read_text().split("\n\n"):
        objects.append(_parse_obj_config(obj, fp))
    return objects


def _parse_obj_config(config: str, orig_file: Path) -> Mapping[str, Any]:
    """Parses a single object's configuration."""
    # the first line will have three leading !, followed by a space and then the object name
    # the next lines will be configuration for that specific object
    # but an object may not have specific configuration either,
    # in which case we only need the name
    obj_config = {}
    root_handler_config = cast(Mapping[str, str], USER_CONFIG.get("handlers", {}))

    lines = config.splitlines()

    if title_match := re.match(TITLE_LINE_RE, lines[0]):
        obj_config["path"] = title_match.group(0)
    else:
        logger.critical(
            f"Invalid title line: {lines[0]}\n in file {orig_file}, skipping"
        )
        return {}

    if len(lines) == 1:
        return {**obj_config, **root_handler_config}

    obj_handler_config = yaml.load("\n".join(lines[1:]), yaml.Loader)

    return {
        **obj_config,
        **{
            **root_handler_config,
            **obj_handler_config,
        },  # union of the root config and object's config
    }


def _run_pytk_on_file(fp: Path) -> Mapping:
    """
    Read a file, convert the objects into the format that pytkdocs expects.
    Then pass that to pytk, and return the parsed output.
    """
    tk_input = {"objects": _get_objects_from_file(fp)}
    tk_output = process_config(tk_input)

    # log any errors that pytkdocs reports
    if load_errs := tk_output.get("loading_errors"):
        for err in load_errs:
            logger.error(err)

    if parse_errs := tk_output.get("parsing_errors"):
        for obj, errs in parse_errs.items():
            for err in errs:
                logger.error(f"Error while parsing {obj}: {err}")

    return tk_output


def _transform_reference_files() -> None:
    """
    Go through all subdirectories/files defined by the user in _reference, and convert them
    into a form that Hugo can render. These generated files will be stored in `content/reference`
    """
