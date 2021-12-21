import re

import semver
from git import Repo
from pybuilder.core import Logger


class NoValidTagFoundError(Exception):
    pass


def find_latest_version_tag(repo: Repo, logger: Logger):
    valid_tags = [t for t in repo.tags if semver.VersionInfo.isvalid(t.name)]
    print(valid_tags)
    logger.debug("Valid tags are: %s", [t.name for t in valid_tags])
    if len(valid_tags) > 0:
        latest_tag = valid_tags[0].name
        if repo.active_branch.name == 'master':
            logger.info("Found latest tag %s", latest_tag)
            return latest_tag
        else:
            branch_tag = f"{latest_tag}-{sane_branch_name(repo.active_branch.name)}"
            logger.info("Found branch tag %s", branch_tag)
            return branch_tag
    else:
        logger.warn("No valid tags found")
        raise NoValidTagFoundError("No valid version tag found")


def sane_branch_name(branch_name):
    if '/' in branch_name:
        branch_part = branch_name.split('/')[-1]
    else:
        branch_part = branch_name
    return re.sub('[^a-z0-9]', '', branch_part.lower())
