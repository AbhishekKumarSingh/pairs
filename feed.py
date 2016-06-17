"""
Feeder module

Takes extracted features from audio and feed it to the elasticsearch apis,
which eventually creates and stores index of all extracted features.
"""

from elasticsearch import Elasticsearch


class Feeder:
    """
    Feeder class that provides helper functions to feed extracted
    features to the elasticsearch inorder to create indexes.
    """
    def __init__(self):
        """
        Initialize Feeder object with elastic search client

        uses localhost, port 9200 as default
        """
        self.es = Elasticsearch()
