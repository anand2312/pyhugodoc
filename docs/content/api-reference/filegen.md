{
    "title": "Filegen",
    "date": "2022-02-18T18:11:59.576921+00:00",
    "draft": false
}

## pyhugodoc.filegen.write\_doc\_file
**Signature**: ```write_doc_file(fp: Path, objects: List[Mapping[str, Any]]) -> None```

Write an object's documentation in the format that Hugo can understand.





## pyhugodoc.filegen.get\_frontmatter
**Signature**: ```get_frontmatter(title: str) -> str```

Get the Hugo frontmatter for a file, in JSON format.


**Parameters:**
- title  _(str)_: The title of the file.

**Returns:**
- str: Hugo compatible frontmatter.
