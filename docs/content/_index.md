---
title: "Home"
date: 2022-01-24T15:21:00+04:00
draft: false
---

# Introduction

{{% notice warning %}}
This tool is rather finicky; working with it will be probably be a pain. Hugo itself doesn't have too many good
documentation themes out there, and not one for an autodocumenting tool like this.
Moreover, this will be an extra command you'll have to remember to run to build your docs (although this should be automated).
All this considered, it might be a good idea to use more mature tools like [MkDocs](https://mkdocs.org) (along with [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)!) or [Sphinx](https://sphinx-doc.org).
Even after this warning, if you decide to use this for whatever reason, feel free to reach out to ask for help:
File an issue, or message me on [Discord](https://discord.com/users/271586885346918400)
{{% /notice %}}

pyhugodoc takes your docstrings, and turns them into markdown files that [Hugo](https://gohugo.io) can then render.
Build beautiful documentation for your Python projects using the wide variety of themes that Hugo offers.

pyhugodoc is inspired by [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings), and uses [pytkdoc](https://github.com/mkdocstrings/pytkdoc) to process docstrings.


# Installation
This tool can be installed with `pip`:
```
pip install -U pyhugodoc
```

If you are using `poetry`:
```
poetry add --dev pyhugodoc
```
