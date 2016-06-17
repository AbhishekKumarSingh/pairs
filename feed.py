"""
Feeder module

Takes extracted features from audio and feed it to the elasticsearch apis,
which eventually creates and stores index of all extracted features.
"""

import json
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

    def readContent(self, jsonFile):
        """
        Converts json data to dictionary format

        Input:
            - jsonFile: a json file containing extracted features of an audio

        output:
            - content: features stored in dictionary format
        """
        with open(jsonFile, 'r') as jf:
            content = json.load(jf)
            return content

    def feed(self, jsonFile, cont_id, iname="audio_index", doc_type="audio"):
        """
        feed extracted features of an audio to elasticsearch for index creation

        Input:
            - jsonFile: a json file of extracted features of an audio
            - cont_id : identity of the content
            - iname   : index name for that group of content
            - doc_type: document type to be stored

        output:
            - retVal: a boolean return value. true if data is indexed otherwise
                      false.
        """
        content = self.readContent(jsonFile)
        ret = self.es.index(index=iname, doc_type, cont_id, body=content)
        retVal = ret['created']
        return retVal
