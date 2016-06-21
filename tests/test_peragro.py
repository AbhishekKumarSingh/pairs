"""
Test peragro module

provides test methods for automated unittesting of peragro module
"""

import unittest
from peragro import PeragroClient
# from elasticsearch import Elasticsearch


class TestPeragroClient(unittest.TestCase):
    """
    unit test PeragroClient module
    """

    def setUp(self):
        """
        set up method for test fixture

        This method runs before each test method. Basically,
        it setups the test environment
        """
        # self.es = Elasticsearch()
        self.c = PeragroClient()
        self.c.index = "temp_index"

    def feed_data(self):
        """
        helper method to feed data to elasticsearch
        """
        self.c.index = "temp_index"
        self.c.es.index(index=self.c.index, doc_type='song', id=1, body={
                'singer': 'Ellie Goulding',
                'title': 'love me like you do',
                'tags': ['cherrytree', 'interscope', 'republic'],
                'release': '7 January 2015',
                'genre': 'electropop',
                'length': 4.12,
                'awesomeness': 0.8
        })

        self.c.es.index(index=self.c.index, doc_type='song', id=2, body={
                'singer': 'Eminem',
                'title': 'love the way you lie',
                'tags': ['Aftermath', 'Interscope', 'shady'],
                'release': '9 August 2010',
                'genre': 'hip hop',
                'length': 4.22,
                'awesomeness': 0.6
        })

        self.c.es.index(index=self.c.index, doc_type='song', id=3, body={
                'singer': 'Arijith Singh',
                'title': 'Tum hi ho',
                'tags': ['romantic', 'movie song track'],
                'release': '2 April 2013',
                'genre': 'romantic',
                'length': 4.15,
                'awesomeness': 0.95
        })

    def tearDown(self):
        """
        setting up tear down method for test fixture

        This method runs after each test method and cleans
        the test environment created in setUp method
        """
        # clean everything stored with temp_index in elastic search
        if self.c.es.indices.exists('temp_index'):
            self.c.es.indices.delete('temp_index')
        # del self.es
        # del self.client

    def test_set_index(self):
        """
        tests set_index method of PeragroClient object
        """
        index = "12ABC54F"
        self.c.set_index(index)

        self.assertEqual(index, self.c.index)

    def test_get_sound(self):
        """
        tests get_sound method of PeragroClient object
        """
        self.feed_data()

        # print "testing get sound"
        # print self.c.es.indices.exists(index='temp_index')
        # print self.c.es.search(index='temp_index', q='tum hi')
        # test when song with that id exists
        id_ = '2'
        sound = self.c.get_sound(id_)
        # print "sound is"
        # print sound

        self.assertEqual(id_, sound['_id'])

        # test when song with that id doesn't exists
        id_ = str(5)
        sound = self.c.get_sound(id_)

        self.assertEqual(sound, None)

    def test_text_search(self):
        """
        tests text_search method of PeragroClient object
        """
        self.feed_data()
        # test simple query

        # test when result present
        query = "tum hi ho"
        # print self.c.es.search(index='temp_index', q=query)
        res = self.c.text_search(query)
        total_hits = res['hits']['total']
        id_ = res['hits']['hits'][0]['_id']
        exp_hits, exp_id = '1', '3'

        self.assertEqual(exp_hits, total_hits)
        self.assertEqual(exp_id, id_)

        # test when no result
        query = "da da da"
        res = self.c.text_search(query)
        total_hits = res['hits']['total']
        count = len(res['hits']['hits'])
        exp_hits, exp_count = '0', '0'

        self.assertEqual(exp_hits, total_hits)
        self.assertEqual(exp_count, count)

        # test the case of field query
        query = "tags:'interscope' genre:'hip hop'"
        res = self.c.text_search(query)
        total_hits = res['hits']['total']
        ids = [res['hits']['hits'][0]['_id'], res['hits']['hits'][1]['_id']]
        exp_hits = '2'
        exp_ids = ['1', '2']
        self.assertEqual(exp_hits, total_hits)
        self.assertListEqual(exp_ids, ids)


if __name__ == '__main__':
    unittest.main()
