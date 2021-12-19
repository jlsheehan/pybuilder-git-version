import os.path
import unittest

from git import Repo

from pybuilder_git_version.util import find_latest_version_tag, NoValidTagFoundError


class TestUtil(unittest.TestCase):

    def test_find_latest_tag(self):
        repo = Repo(os.getcwd())
        latest_version_tag = find_latest_version_tag(repo, None)
        self.assertRaises(NoValidTagFoundError)