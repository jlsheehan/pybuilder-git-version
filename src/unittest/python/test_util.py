import logging

import pytest
from git import Repo, TagReference, Commit

from pybuilder_git_version.util import find_latest_version_tag, NoValidTagFoundError, sane_branch_name

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
    tag3.name = '0.0.3'
    repo = mocker.Mock(Repo)
    repo.tags = [tag1, tag2, tag3]
    repo.active_branch.name = 'master'
    repo.is_dirty.return_value = False
    repo.iter_commits.return_value = [tag3.commit, tag2.commit, tag1.commit]
    assert find_latest_version_tag(repo, logger) == '0.0.3'


def test_valid_dev_tag(mocker):
    tag1 = mocker.Mock(TagReference)
    tag1.name = '0.0.1'
    tag2 = mocker.Mock(TagReference)
    tag2.name = '0.0.2'
    tag3 = mocker.Mock(TagReference)
    tag3.name = '0.0.3'
    latest_commit = mocker.Mock(Commit)
    repo = mocker.Mock(Repo)
    repo.tags = [tag1, tag2, tag3]
    repo.active_branch.name = 'develop'
    repo.is_dirty.return_value = False
    repo.iter_commits.return_value = [latest_commit, tag3.commit, tag2.commit, tag1.commit]
    assert find_latest_version_tag(repo, logger) == '0.0.4+develop.1'


def test_sane_branch_name():
    assert sane_branch_name('feature/TICKET-100') == 'ticket100'
    assert sane_branch_name('hotfix/ComPlex-=?Pr_oble,m') == 'complexproblem'
