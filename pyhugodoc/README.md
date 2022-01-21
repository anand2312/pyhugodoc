# Implementatin Detail Documentation

Here I write about stuff relevant to the implementation.

## pytkdocs output format

### Parsed Docstring format
```
docstring_sections: [
    {
        type: markdown
        value: The main part of the docstring, which is not in any section.
    },
    {
        type: parameters | return
        annotation: annotation as a string
        name: param name (this doesn't exist for return)
        kind: POSITIONAL / POSITIONAL_OR_KEYWORD and so on
        description: description of the argument/return
    }
]
