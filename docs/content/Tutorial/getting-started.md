---
title: "Getting started"
date: 2022-02-18T22:13:45+04:00
draft: false
---

### Create Hugo Project

Just like any other Hugo site, you first need to create a new Hugo project.
Follow [Hugo's documentation](https://gohugo.io/getting-started/quick-start/) for more information.


### Configuration

The gist of how pyhugodocs works: you list the objects to be documented in a "reference directory" (usually called `_api-reference`). This folder is set to be ignored by Hugo (you have to add that to your `config.toml`!)
pyhugodoc then reads these objects, gets their docstrings, and generates a `api-reference` folder automatically.
_This_ is the folder that Hugo will render.

{{% notice tip %}}
Check out pyhugodoc's GitHub repository for a sample!
{{% /notice %}}

Once you have installed `pyhugodoc`, you need to create a config file to tell it where to look for
content.
The config file should be called `pyhugodoc.yaml` and should be in the root of your repository.

Sample:
```yaml
site_dir: docs  # the name of the folder in which the Hugo site is
reference_dir: content/_api-reference  # path to reference dir, relative to site_dir
docstring_style: google  # the docstring style used; can be google or numpy
```
