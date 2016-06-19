"""
Test Feeder module

Provides test methods for automated unit testing of Feeder module
"""

import os
import json
import string
import random
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
        # clean everything stored with test_index in elastic search
        if self.feeder.es.indices.exists('test_index'):
            self.feeder.es.indices.delete('test_index')
        del self.feeder

    def test_readContent(self):
        """
        tests readContent method of Feeder object
        """
        data = {
                'singer': 'Ellie Goulding',
                'title': 'love me like you do',
                'tags': ['cherrytree', 'interscope', 'republic'],
                'release': '7 January 2015',
                'genre': 'electropop',
                'length': 4.12,
                'awesomeness': 0.8
            }

        # use the temporary file and then clean it up after operation
        fd, path = tempfile.mkstemp()
        try:
            with os.fdopen(fd, 'w') as tmp:
                jsonDump = json.dumps(data)
                tmp.write(jsonDump)
                tmp.close()
                content = self.feeder.readContent(path)
                self.assertDictEqual(data, content)
        finally:
            os.remove(path)

    def id_generator(self, size=10, chars=string.ascii_uppercase +
                     string.digits):
        """
        generate random token of given size
        """
        tok = ''.join(random.SystemRandom().choice(
            string.ascii_uppercase + string.digits) for _ in range(size))
        return tok

    def test_feed(self):
        """
        tests feed method of Feeder object
        """
        iname = "test_index"
        doc_type = "test_doc"
        cont_id = self.id_generator()

        data = {
                'singer': 'Ellie Goulding',
                'title': 'love me like you do',
                'tags': ['cherrytree', 'interscope', 'republic'],
                'release': '7 January 2015',
                'genre': 'electropop',
                'length': 4.12,
                'awesomeness': 0.8
            }

        # use temporary file and clean it up after operation
        fd, path = tempfile.mkstemp()
        with os.fdopen(fd, 'w') as tmpfile:
            jsonDump = json.dumps(data)
            tmpfile.write(jsonDump)
            tmpfile.close()
            retVal = self.feeder.feed(path, cont_id, iname, doc_type)
            self.assertTrue(retVal)
            self.assertTrue(self.feeder.es.indices.exists('test_index'))


if __name__ == '__main__':
    unittest.main()
