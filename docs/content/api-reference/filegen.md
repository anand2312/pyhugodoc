{
    "title": "Filegen",
    "date": "2022-02-15T18:16:07.272565+00:00",
    "draft": false
}

## pyhugodoc.filegen.write_doc_file
**Signature**: ```write_doc_file(fp: Path, objects: List[Mapping[str, Any]]) -> None```

Write an object's documentation in the format that Hugo can understand.




## pyhugodoc.filegen.get_frontmatter
**Signature**: ```get_frontmatter(title: str) -> str```

Get the Hugo frontmatter for a file, in JSON format.

**Parameters:**
- title  _(str)_:The title of the file.

**Returns:**
- str: Hugo compatible frontmatter.
