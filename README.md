# pyhugodoc

Create beautiful documentation for your Python projects, with Hugo, the static-site generator.
pyhugodoc will read docstrings from your source code and create files that Hugo will then
convert into static HTML.

**This project is heavily inspired by [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)**. Thanks for the great work!

This project is a WIP and everything is very finnicky.

## Usage

pyhugodoc uses `pytkdocs` under the hood (this entire project takes a lot of inspirations from mkdocstrings);
It can read docstrings written in either `google` or `numpy` style.

This is the usage that I am imagining right now:

1) Set up hugo site in your project's root directory.
```
hugo new site docs
```
This creates a new hugo site in the `docs` directory.

The content for the site will be in the `content` directory (automatically made by hugo after the above command).
To list the methods/classes that need to be documented, make a folder called `_reference` in the `content` directory.
pyhugodoc will read the files in this `_reference` folder, get their docstrings from your source code, and turn them into
files that Hugo can then render.

2) Create `pyhugodoc.yaml` configuration file
```yaml
site_dir: docs # the Hugo site directory
reference_dir: content/_references # path relative to site_dir
docstring_style: google
```

3) Start writing documentation!
pyhugodoc will read the docstrings from your source code.
For example, to document two classes, `my_lib.src.Example` and `my_lib.Exception`,
- Make a file in the `_reference` folder, say `example.md` with the following
```
::: my_lib.src.Example

::: my_lib.Exception
```

4) Once you're done, run `pyhugodoc generate`.

5) Build the site like any other Hugo site!
