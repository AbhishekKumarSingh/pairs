"""
Test Feeder module

Provides test methods for automated unit testing of Feeder module
"""

import tempfile
import unittest
from feed import Feeder


class TestFeeder(unittest.TestCase):
    """
    Test Feeder class for unittesting Feeder module
    """
    def setUp(self):
        """
        set up method for test fixture

        This method runs before each test method. Basically,
        it setups the test environment
        """
        self.feeder = Feeder()

    def tearDown(self):
        """
        set up tear down method for test fixture

        This method runs after each test method and cleans
        the test environment created in setUp method
        """
        del self.feeder

    def test_readContent(self):
        """
        """
        jsonData = "{
                'singer': 'Ellie Goulding',
                'title': 'love me like you do',
                'tags': ['cherrytree', 'interscope', 'republic'],
                'release': '7 January 2015',
                'genre': 'electropop',
                'length': 4.12,
                'awesomeness': 0.8
            }"

        # use the TemporaryFile context manager for easy clean-up
        with tempfile.TemporaryFile() as tmp:
            tmp.write(jsonData)
            content = self.feeder.readContent(tmp)
            self.assertDictEqual(jsonData, content)
