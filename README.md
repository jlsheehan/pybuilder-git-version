PyBuilder Git Version Plugin
============================

Summary
-------

This project is a plugin for [PyBuilder](https://pybuilder.io) that sets the
project version based on git tags.

Usage
-----

To use the plugin put the following in the plugins section of `build.py`:

```python
use_plugin('pybuilder_git_version')
```

The possible properties for use are:

| Property                                    | Value        | Default | Usage                                      |
|---------------------------------------------|--------------|---------|--------------------------------------------|
| use_git_version                             | True / False | True    | Turns off pybuilder_git_version            |
| git_version_commit_distance_as_build_number | True / False | True    | Uses commit count from tag as build number |


Examples
--------

The following table has examples of repo state and corresponding version
number produced.

| Tag        | Branch             | Clean / Dirty | Number of commits since tag | Version                |
|------------|--------------------|---------------|-----------------------------|------------------------|
| 0.0.1      | master             | clean         | 0                           | 0.0.1                  |
| 0.0.1      | master             | dirty         | 0                           | 0.0.2+build.0          |
| 0.2.2      | develop            | clean         | 5                           | 0.2.3+develop.5        |
| 1.2.3      | develop            | dirty         | 3                           | 1.2.4+develop.3        |
| 1.0.0-rc.1 | feature/TICKET-100 | clean         | 5                           | 1.0.0-rc.1+ticket100.5 |
| 0.0.1      | hotfix/BUG-20      | clean         | 0                           | 0.0.2+bug20.0          |