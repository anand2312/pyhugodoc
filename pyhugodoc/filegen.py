import json
import logging

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, List, Mapping


log = logging.getLogger(__name__)


def write_doc_file(fp: Path, objects: List[Mapping[str, Any]]) -> None:
    """Write an object's documentation in the format that Hugo can understand."""
    # the file path passed to these functions should be the final markdown file paths
    log.info(f"Building documentation for {fp}")
    title = fp.stem
    frontmatter = get_frontmatter(title)
    obj_docs = [_tk_obj_to_content(obj) for obj in objects]

    content = f"{frontmatter}\n\n"
    content += "\n\n".join(obj_docs)

    with open(fp, "w") as f:
        f.write(content)


def get_frontmatter(title: str) -> str:
    """
    Get the Hugo frontmatter for a file, in JSON format.

    Args:
        title: The title of the file.
    Returns:
        Hugo compatible frontmatter.
    """
    ts = datetime.now(timezone.utc).isoformat()
    title = title.replace("-", " ").replace("_", " ").title()

    return json.dumps({"title": title, "date": ts, "draft": False}, indent=4)


def _tk_obj_to_content(data: Mapping[str, Any]) -> str:
    # if the object is a function or a class, give it a level-2 header
    # and use it's fully qualified path as the header
    # if it is a method or a property, give it a level-4 header
    # and use just it's name as the header

    props = data["properties"]
    path = data["path"]
    name = data["name"]
    category = data["category"]

    log.info(f"Converting object {path}")

    if category in ["class", "function"]:
        head = f"## {path}"
    else:
        head = f"#### {name}"

    # join on the special properties to the side
    if props:
        head += f" _({', '.join(props)})_"

    body = f"**Signature**: ```{_fn_signature(name, data['signature'])}```"
    body += "\n\n"

    for section in data["docstring_sections"]:
        if section["type"] == "markdown":
            # main function definition
            body += section["value"]
            body += "\n"
        elif section["type"] == "parameters":
            # param descriptions
            body += "**Parameters:**\n"
            for param in section["value"]:
                elem = f"- {param['name']} "
                annotation = param["annotation"]
                elem += f" _({annotation})_:" if annotation else ":"
                elem += param["description"]
                elem += "\n"

                body += elem
            body += "\n"
        elif section["type"] == "return":
            body += "**Returns:**\n"
            return_annt = section["value"]["annotation"]
            body += f"- {return_annt}: " if return_annt else ""
            body += section["value"]["description"]
        elif section["type"] == "exception":
            body += "**Raises:**\n"
            for exc in section["value"]:
                elem = f"- {exc['annotation']}: {exc['description']}"
        else:
            log.warning(f"Unknown docstring section {section['type']}; skipping...")

    body += "\n"
    out = f"{head}\n{body}"

    # recursively convert all child members, if any
    children_converted = [
        _tk_obj_to_content(child_data) for child_data in data["children"].values()
    ]
    joined = "\n\n".join(children_converted)

    return out + "\n" + joined


def _fn_signature(fn_name: str, data: Mapping[str, Any]) -> str:
    param_strings = []

    for param in data["parameters"]:
        out = ""
        kind, name, annt, default = (
            param["kind"],
            param["name"],
            param.get("annotation"),
            param.get("default"),
        )

        if kind == "KEYWORD_ONLY":
            out += "*, "
        elif kind == "POSITIONAL_ONLY":
            out += f"/, "

        out += f"{name}{': ' + annt if annt else ''}"
        out += f" = {default}" if default else ""
        param_strings.append(out)

    return_ann = data.get("return_annotation")

    return f"{fn_name}({', '.join(param_strings)}) {'-> ' + return_ann if return_ann else ''}"
