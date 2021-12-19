import semver
from git import Repo
from pybuilder.core import Logger


class NoValidTagFoundError(Exception):
    pass


def find_latest_version_tag(repo: Repo, logger: Logger):
    valid_tags = list(map(lambda t: t.name, filter(lambda t: semver.VersionInfo.isvalid(t.name), repo.tags)))
    logger.debug("Valid tags are: %s", valid_tags)
    if len(valid_tags) > 0:
        latest_tag = valid_tags[0]
        logger.info("Found latest tag %s", latest_tag)
        return latest_tag
    else:
        logger.warn("No valid tags found")
        raise NoValidTagFoundError("No valid version tag found")
