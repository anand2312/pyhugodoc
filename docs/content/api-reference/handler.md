{
    "title": "Handler",
    "date": "2022-02-15T18:16:07.272565+00:00",
    "draft": false
}

## pyhugodoc.handler._get_objects_from_file _(private)_
**Signature**: ```_get_objects_from_file(fp: Path) -> List[Mapping[str, Any]]```

Read a file from the user-defined _references directory, and get the objects
defined in it.

**Parameters:**
- fp  _(Path)_:The path to the file to be parsed

**Returns:**
- List[Mapping[str, Any]]: Parsed object configurations, to be passed to pytkdocs.



## pyhugodoc.handler._transform_reference_files _(private)_
**Signature**: ```_transform_reference_files() -> None```

Go through all subdirectories/files defined by the user in _reference, and convert them
into a form that Hugo can render. These generated files will be stored in `content/reference`
