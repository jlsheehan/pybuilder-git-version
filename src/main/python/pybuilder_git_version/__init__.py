from git import Repo
from pybuilder.core import init, Project, Logger

import pybuilder_git_version.util


@init
def init_pybuilder_git_version(project: Project, logger: Logger):
    project.set_property_if_unset("use_git_version", True)
    if project.get_property("use_git_version"):
        repo = Repo(project.basedir)
        latest_tag = pybuilder_git_version.util.find_latest_version_tag(repo, logger)
        project.version = latest_tag
        project.set_property("dir_dist", f"$dir_target/dist/{project.name}-{project.version}")
        logger.info("Set project version to %s", project.version)
    else:
        logger.debug("Not using git version")
