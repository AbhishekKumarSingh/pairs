"""
python script to take downloaded FreeSound audio (found by matching all
*.json files in a folder) and produce 10-second snippets from each one,
as long as they match our requirements
"""

import os
import sys
import json
import glob
import subprocess
import shutil
import random
import math
# from scikits.audiolab import Sndfile
# from scikits.audiolab import Format

###############################################################
# User settings
frmfolder = 'soundsgot'
toofolder = '10sec'
numfolds = 10

oklicences = [
    u'http://creativecommons.org/licenses/by/3.0/',
    u'http://creativecommons.org/publicdomain/zero/1.0/',
    ]

okencodings = [
    'pcm16',
    'pcm24',
    'pcm32',
    ]

okbitdepths = [16, 24, 32]
maxnumchannels = 2

targetduration = 10.

reallydoit = True


###############################################################
# preliminaries
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == os.errno.EEXIST:
            pass
        else:
            raise


def integertofoldpath(whichone):
    whichfold = (whichone % numfolds) + 1
    return "%s/%.2i" % (toofolder, whichfold)

for whichone in range(numfolds):
    mkdir_p(integertofoldpath(whichone))

###############################################################
# let's go
itemstouse = []
durations = {}  # id---->duration
for jsonpath in glob.glob("%s/*.json" % frmfolder):
    wavpath = "%s.wav" % os.path.splitext(jsonpath)[0]
    itemid = os.path.splitext(os.path.basename(jsonpath))[0]

    # check the json - licence ok
    jsonfp = open(jsonpath, 'r')
    jsondata = json.load(jsonfp)
    jsonfp.close()
    #print jsondata[u'license']
    if jsondata[u'license'] not in oklicences:
        print "Skip %s due to licence: %s" % (itemid, jsondata[u'license'])
        continue

    # check the wav metadata - bitdepth ok, numchans ok
    # Incase if audiolab is used
    """
    sf = Sndfile(wavpath, "r")
    if (sf.channels > maxnumchannels):
        print "Skip due to num channels: %i" % sf.channels
        continue
    if (sf.encoding not in okencodings):
        print "Skip due to encoding: %s" % sf.encoding
        continue

    print sf
    print sf.format
    # also get duration, used later
    duration = sf.nframes / sf.samplerate
    print "Duration %g" % duration
    """

    # need to use soxi instead (-D for dur, -b for bit depth, -c for numchans)
    duration = float(subprocess.check_output(["soxi", "-D", wavpath]))
    # print "Duration %g" % duration
    numchans = int(subprocess.check_output(["soxi", "-c", wavpath]))
    # print "Num channels %i" % numchans
    bitdepth = int(subprocess.check_output(["soxi", "-b", wavpath]))
    # print "Num channels %i" % bitdepth
    if (numchans > maxnumchannels):
        print "Skip %s due to num channels: %i" % (itemid, numchans)
        continue
    if (bitdepth not in okbitdepths):
        print "Skip %s due to bitdepth: %s" % (itemid, bitdepth)
        continue
    if (duration < targetduration):
        print "Skip %s due to duration: %g" % (itemid, duration)
        continue

    # if acceptable, add the ID number (string) to the list
    itemstouse.append(itemid)
    durations[itemid] = duration

random.seed(97867564)  # this is to make the foldwise split repeatable
random.shuffle(itemstouse)

# to make balanced folds, round down
itemstouse = itemstouse[:(numfolds * int(math.floor(len(itemstouse) /
                                                    float(numfolds))))]

print "Will make %i snippets" % len(itemstouse)

for whichone, itemid in enumerate(itemstouse):
    foldpath = integertofoldpath(whichone)
    # copy the metadata
    print "cp %s/%s.json %s/%s.json" % (frmfolder, itemid, foldpath, itemid)
    if reallydoit:
        shutil.copyfile("%s/%s.json" % (frmfolder, itemid), "%s/%s.json" % (
            foldpath, itemid))
    # construct sox command to make N-sec excerpt
    soxcmd = ["sox", "%s/%s.wav" % (frmfolder, itemid),
              "-c", "1", "-r", "44100", "-b", "16",
              "%s/%s.wav" % (foldpath, itemid),
              "trim", str(max(0, durations[itemid]-targetduration) * 0.5),
              str(targetduration), "gain", "-n", "-2"]
    print soxcmd
    if reallydoit:
        subprocess.call(soxcmd)

# check that we have the exact number of json and wav files we expected
numjsons = len(glob.glob("%s/*/*.json" % toofolder))
numwavs = len(glob.glob("%s/*/*.wav" % toofolder))
if reallydoit and ((numjsons != len(itemstouse)) or (numwavs != len(itemstouse))):
    raise RuntimeError("The resulting number of JSON and WAV files is not as expected. Should have created %i, but found %i json and %i wav." \
		% (len(itemstouse), numjsons, numwavs))
