"""
Given dataset of audio, extract features and build index
"""

import os
import sys
import glob
from extractor import FeatureExtractor
from feed import Feeder
from peragro import PeragroClient


def getAll_audio(source_dir, extension='wav'):
    """
    returns the list of all audio files

    search for all the audios from top dir by matching
    the pattern provided.
    """
    audioFiles = glob.glob(source_dir + "/*/*." + extension)
    return audioFiles


if __name__ == '__main__':
    source_dir = sys.argv[1]
    output_dir = "features"

    fe = FeatureExtractor("gen")

    audioFiles = getAll_audio(source_dir)

    print "started feature extraction..."
    for af in audioFiles:
        filename = os.path.basename(af).split(".")[0] + ".json"
        oFile = os.path.join(output_dir, filename)
        fe.extract(af, oFile)

    print "feature extraction complete"
    print "features stored in %s directory" % output_dir

    f = Feeder()

    dir_path = output_dir

    # index creation
    print "started index creation..."
    f.feedAll(dir_path, iname="audio_index", doc_type="audio")
    print "index creation complete"

    client = PeragroClient()
    client.set_index('audio_index')

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
    # f.es.indices.delete(index="example_index")
