import logging

import pytest
from git import Repo, TagReference

from pybuilder_git_version.util import find_latest_version_tag, NoValidTagFoundError

logger = logging.getLogger(__name__)


def test_no_valid_tag(mocker):
    tag1 = mocker.Mock(TagReference)
    tag1.name = 'Initial commit'
    tag2 = mocker.Mock(TagReference)
    tag2.name = 'foo bar'
    repo = mocker.Mock(Repo)
    repo.tags = [tag1]
    repo.is_dirty.return_value = False
    with pytest.raises(NoValidTagFoundError):
        find_latest_version_tag(repo, logger)


def test_valid_tag(mocker):
    tag1 = mocker.Mock(TagReference)
    tag1.name = '0.0.1'
    tag2 = mocker.Mock(TagReference)
    tag2.name = '0.0.2'
    tag3 = mocker.Mock(TagReference)
    tag3.name = '0.0.3-beta'
    repo = mocker.Mock(Repo)
    repo.tags = [tag3, tag2, tag1]
    repo.active_branch.name = 'master'
    repo.is_dirty.return_value = False
    assert '0.0.3-beta' == find_latest_version_tag(repo, logger)


def test_valid_branch_tag(mocker):
    tag1 = mocker.Mock(TagReference)
    tag1.name = '1.0.2'
    repo = mocker.Mock(Repo)
    repo.tags = [tag1]
    repo.active_branch.name = 'feature/TICKET-100'
    repo.is_dirty.return_value = False
    assert find_latest_version_tag(repo, logger) == '1.0.2-ticket100'


def test_dirty_branch(mocker):
    tag1 = mocker.Mock(TagReference)
    tag1.name = '0.0.1'
    tag2 = mocker.Mock(TagReference)
    tag2.name = '0.0.2'
    tag3 = mocker.Mock(TagReference)
    tag3.name = '0.0.3'
    repo = mocker.Mock(Repo)
    repo.tags = [tag3, tag2, tag1]
    repo.is_dirty.return_value = True
