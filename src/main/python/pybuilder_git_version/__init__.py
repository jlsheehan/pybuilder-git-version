import semver
from git import Repo
from pybuilder.core import init, Project, Logger, task

import pybuilder_git_version.util
from git.exc import InvalidGitRepositoryError

@init
def init_pybuilder_git_version(project: Project, logger: Logger):
    project.set_property_if_unset("use_git_version", True)
    if project.get_property("use_git_version"):
        try:
            repo = Repo(project.basedir)
            latest_tag = pybuilder_git_version.util.find_latest_version_tag(repo, logger)
            project.version = latest_tag.name
            project.set_property("dir_dist", f"$dir_target/dist/{project.name}-{project.version}")
            logger.info("Set project version to %s", project.version)
        except InvalidGitRepositoryError:
            logger.warn("No git repository found")
    else:
        logger.debug("Not using git version")


@task
def bump_version(project: Project, logger: Logger):
    repo = Repo(project.basedir)
    latest_tag = util.find_latest_version_tag(repo, logger)
    semver.bump_patch(latest_tag.name)
    repo.create_tag('refs/head/master', ref='HEAD', message='1.1.1.1')
    pass