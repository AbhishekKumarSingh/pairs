"""
Get sounds and their metadata from freesound

based on tagsearch results it downloads sounds and their metadata from
freesound.org. Metadata is stored in json file format. File format is like:
sound_id.json
"""


import os.path
import json
import time

from freesound import Freesound, Sound
from localdata import freesound_api_key


Freesound.set_api_key(freesound_api_key)

##################################
# settings:
tagsearch = "field-recording"
outfolder = 'soundsgot'
maxpages = 1e99
audiotype = "wav"
minduration = 10
startpage = 0

##################################
# start search
fquery = "tag:%s type:%s duration:[%g TO *]" % (tagsearch, audiotype,
                                                minduration)
print fquery
pager = Sound.search(f=fquery)

print pager.keys()
print "Num results: %i" % pager['num_results']
print "Num pages  : %i" % pager['num_pages']

for whichpage in range(min(maxpages, pager['num_pages'])):
    print "----- PAGE %i -----" % (whichpage + 1)
    if (whichpage + 1) < startpage:
        pager.next()
        continue

    for s in pager['sounds']:
        thesound = Sound.get_sound(s['id'])
        print "%i %s %s" % (s['id'], s['original_filename'], s['url'])
        outfname = "%i.%s" % (s['id'], audiotype)
        jsonfpath = "%s/%i.json" % (outfolder, s['id'])
        if os.path.isfile(jsonfpath):
            print "           already got"
        else:
            thesound.retrieve(outfolder, outfname)
            # also write metadata to file
            jsonf = open(jsonfpath, 'w')
            # we can't serialise the object directly, so add some of its keys
            # to the search result which we'll serialise
            for key in ['license', 'samplerate', 'channels', 'geotag']:
                try:
                    s[key] = thesound[key]
                except:
                    pass
            jsonf.write(json.dumps(s))
            jsonf.close()
            time.sleep(1)

    print
    pager.next()

print "Done."
