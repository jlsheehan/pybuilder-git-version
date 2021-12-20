import logging
import os.path

import pytest
from git import Repo

from pybuilder_git_version.util import find_latest_version_tag, NoValidTagFoundError

logger = logging.getLogger(__name__)


def test_find_latest_tag():
    repo = Repo(os.getcwd())
    with pytest.raises(NoValidTagFoundError):
        latest_version_tag = find_latest_version_tag(repo, logger)
