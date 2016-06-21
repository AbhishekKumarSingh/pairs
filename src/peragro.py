"""
A client that provides audio search

provides different api(s) for audio search, including text based and content
based search.
"""

from elasticsearch import Elasticsearch


class PeragroClient():
    """
    An audio search client
    """
    def __init__(self):
        """
        initialize client object with elasticsearch object
        """
        self.es = Elasticsearch()

    def set_index(self, index):
        """
        set index for to lookup in elasticsearch

        Input:
            -index: an elasticsearch index
        """
        self.index = index

    def get_sound(self, id_):
        """
        Get sound by its id

        input:
            -id: id of sound

        output:
            -sound: sound details if it exists otherwise None

        Usage:

        >>> id = "X2VFAB12GH"
        >>> sound = c.get_sound(id)
        """
        if self.es.exists(index=self.index, doc_type='_all', id=id_):
            res = self.es.get(index=self.index, id=id_)
            return res
        else:
            return None

    def text_search(self, query):
        """
        Get sound results based on text query.
        It also has support for field queries.

        Usage:

        >>> query = "tum hi ho"
        >>> sounds = c.text_search(query)

        >>> # OR field query
        >>> query = "tags:'interscope' genre:'hip hop'"
        >>> sounds = c.text_search(query)
        """
        # print self.index
        # print self.es.search(index=self.index)
        res = self.es.search(index=self.index, q=query)
        print("Got %d Hits:" % res['hits']['total'])
        return res

    #def text_search(self, query, fields):
    #    """
    #    fields parameter allows to specify the information
    #    you want in the results list
    #    """
    #    pass

    #def text_search(self, query, filter, fields):
    #    """
    #    search based on filter
    #    """
    #    pass
