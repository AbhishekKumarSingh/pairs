"""
Given acoustic dataset of features, build index
"""

import os
import sys
import glob
from feed import Feeder
from peragro import PeragroClient


def getAll_audioDir(source_dir, extension='json'):
    """
    returns the list of all the directory with audio feature files (json files)

    search for all the json files from top dir by matching the
    pattern provided.
    """
    audioFiles = glob.glob(source_dir + "/*/*/*." + extension)
    audioDir = []
    for af in audioFiles:
        d = os.path.dirname(af)
        audioDir.append(d)
    return audioDir


if __name__ == "__main__":
    source_dir = sys.argv[1]

    audioDir = getAll_audioDir(source_dir)

    f = Feeder()

    # index creation
    print "started index creation"

    for ad in audioDir:
        f.feedAll(ad, iname='ab_index', doc_type='ab_data')

    print "index creation complete"

    client = PeragroClient()
    client.set_index('ab_index')

    while True:
        print "[1] search by id"
        print "[2] search by text"
        print "[3] quit"

        choice = raw_input("Enter your choice: ")

        if choice == '1':
            id_ = raw_input("Enter id: ")
            res = client.get_sound(id_)

            if res:
                print res['_id'], "found"
            else:
                print id_, "not found"

        elif choice == '2':
            q = raw_input("Enter query: ")
            res = client.text_search(q)

        elif choice == '3':
            break

    # clear the indexes
    # f.es.indices.delete(index="ab_index")
