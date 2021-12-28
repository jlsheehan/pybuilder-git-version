#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.flake8")
use_plugin("python.distutils")
use_plugin("pypi:pybuilder_pytest")
use_plugin('pypi:pybuilder_pytest_coverage')

authors = [Author("Jeffrey Sheehan", "jeff.sheehan7@gmail.com")]
summary = "A Git versioning plugin for PyBuilder"
with open('README.md') as readme:
    description = readme.read()
url = "https://github.com/jlsheehan/pybuilder-git-version"

name = "pybuilder-git-version"
default_task = "publish"
version = '0.1.4'

@init
def set_properties(project):
    project.depends_on("gitpython==3.1.24")
    project.depends_on("semver==2.13.0")
    project.build_depends_on("pytest")
    project.build_depends_on("pytest-mock")
