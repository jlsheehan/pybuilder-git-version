#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
# use_plugin("python.coverage")
use_plugin("python.distutils")


name = "pybuilder-git-version"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on("gitpython==3.1.24")
    project.depends_on("semver==2.13.0")

    for prop in project.properties:
        print("{}:{}".format(prop, project.get_property(prop)))
