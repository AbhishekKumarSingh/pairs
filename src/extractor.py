"""
Feature extractor module

Extracts lowlevel and highlevel features from audio
using the essentia toolkit and returns it in json format.
"""

import os
import errno
import glob
import subprocess


def make_p(path):
    """
    make sure path exists. If path doesn't exists then
    create the path else ignore.
    """
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


class FeatureExtractor:
    """
    FeatureExtractor class that provides helper functions to
    extract lowlevel and highlevel features from audio.
    """
    def __init__(self, type):
        """
        Initialize FeatureExtractor object with the provided
        type of extractor.
        """
        if type == "gen":
            self.ex = "bin/streaming_extractor_music"

    def extract(self, inputFile, outputFile, profile=None):
        """
        extract features from an audio.

        Input:
            - inputFile: an audio file path
            - outputFile: a json file path
            - profile: profiler file which contains configuration
                       information.
        """
        dir_name = os.path.dirname(outputFile)

        if dir_name:
            # check if path exists, if not then create
            make_p(dir_name)

        if not profile:
            subprocess.call([self.ex, inputFile, outputFile])
        else:
            subprocess.call([self.ex, inputFile, outputFile, profile])

    def extractAll(self, source_dir, output_dir, ext, profile=None):
        """
        extract features of all audio present in the source_dir
        and writes its features to json file inside output_dir

        Input:
            - source_dir: directory containing audioes
            - output_dir: directory to write json files to
            - ext: extension of audio file. eg: wav, mp3 etc
        """
        audioFiles = glob.glob(source_dir + "/*." + ext)

        if not audioFiles:
            print "No audio found."
            return

        make_p(output_dir)

        for inFile in audioFiles:
            filename = os.path.basename(inFile).split(".")[0] + ".json"
            oFile = os.path.join(output_dir, filename)
            self.extract(inFile, oFile, profile)
