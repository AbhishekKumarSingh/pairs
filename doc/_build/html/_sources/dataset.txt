Audio dataset creation
======================

Dataset is created using the scripts in the `data_gen` directoy. Based on tag search audio is searched and downloaded from the [freesound](http://freesound.org) along with their metadata. And then produced 10-second snippets from each one, as long as they matches the requirements. Data were also sampled from the downloaded set.

This dataset contains 7690 10-second audio files in a standardised format,
extracted from contributions on the Freesound archive which were labelled with
the "field-recording" tag. Note that the original tagging (as well as the audio
submission) is crowdsourced, so the dataset is not guaranteed to consist purely
of "field recordings" as might be defined by practitioners. The intention is to
represent the content of an archive collection on such a topic, rather than to
represent a controlled definition of such a topic.

Each audio file has a corresponding text file, containing metadata such as
author and tags. 
The dataset has been randomly split into 10 equal-size subsets. This is so that
you can perform 10-fold crossvalidation in machine-learning experiments, or can
use fixed subsets of the data (e.g. use one subset for development, and others
for later validation). Each of the 10 subsets has about 128 minutes of audio;
the dataset totals over 21 hours of audio.


FILE FORMATS AND LAYOUT
-----------------------

The dataset is partitioned into 10 subsets with an equal number of audio files
in each. You may have these as zipfiles or as folders, named 01 02 03 04 05 06
07 08 09 10.

Each .wav file contained within has a numeric ID as a filename, which
corresponds to the ID of the original audio file held in the Freesound archive.
Note that the .wav file is NOT the same as the one on Freesound - it has been
excerpted and standardised. Each .wav file is 10 seconds long, WAV, mono,
sample rate 44.1 kHz, 16-bit PCM, amplitude normalised. The numeric ID used for
filenames does not have a fixed number of digits but is as many as 6-digit.

Each .wav file also has a corresponding .json file, which is simply the
metadata reported by the Freesound server while fetching the original audio.
Notable keys are:

* user: the username and url for the Freesound user who uploaded this particular
  audio file. The copyright in the audio file remains with them.
* license: the license of the audio file.
* tags: the list of tags associated with the file. "field-recording" will be but one.
* id: the Freesound ID - should match filename.
* url: a URL that takes you to the Freesound item page.
* geotag: a lat/lon pair indicating geolocation. Roughly one-third of the files
  include this tag - availability of geotag was not a criterion for constructing the dataset.


The JSON data includes fields such as "channels", "duration",
"samplerate" - these refer to the original audio contribution,
and not to the excerpt included here.


get_sound module:
------------------

This module is responsible for getting sound and their metadata based on tagsearch results from freesound.org. Metadata is stored in json file format. File format is like metadata for audio having id as `12345` has its metadata stored in `12345.json` file.

snippetmaker module:
---------------------

This module is responsible for generating 10-second snippets from each one of the downloaded audios.

Installing dependencies
-----------------------

1. make virtual environment inside `data_gen` directory:

        .. code-block:: bash

            $ virtualenv env


2. activate virtual environment

        .. code-block:: bash

            $ source env/bin/activate


3. install requirements form `requirements.txt`

        .. code-block:: bash

            $ pip install requirements.txt


4. clone freesound python bindings `freesound-python`

        .. code-block:: bash

            $ git clone https://github.com/danstowell/freesound-python


5. install `freesound-python` inside virtual environment

        .. code-block:: bash

            # when your virtual environment is active
            $ python setup.py install


Procedure to run the modules
----------------------------

`Note`: module get_sound.py performs heavy hits on freesound server. please take permission from freesound before hand.

Get freesound api token
***********************

To authenticate API calls with the token strategy you’ll need to create a Freesound account (if you don’t have one yet!) and request a new API credential by visiting http://www.freesound.org/apiv2/apply. In this page you’ll see a table with all API credentials you have requested plus some other information. You should use the keys in ‘Client secret/Api key’ column, which are long alphanumeric strings. You should get a different API key for every application you develop.

Add freesound client api key
*****************************

replace null string with acutal client_api_key in `local_data.py`


    .. code-block:: python

        freesound_api_key = <client_api_key>



Run modules
************


    .. code-block:: bash

        $ python get_sound.py
        $ python snippetmaker.py
