.. peragro_airs documentation master file, created by
   sphinx-quickstart on Tue Jun 21 21:13:57 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Peragro Audio Information Retrieval System (PAIRS) documentation!
============================================================================

Introduction
-------------

Purpose
********

“Search, and you will find”

Implementation of an audio search system for Peragro. An Audio Information
Retrieval(AIR) system that would provide client API(s) for audio search and
information retrieval. Search will be based on annotated text/descriptions or
tags/labels associated with an audio as well as on low and high level features.
Focus is to implement an AIR system that provides text based and content based
search. Users would be able to perform query through the provided client API(s)
and will get list of relevant audios in return.

Benefits
********

* Provides client API(s) for text and content based search. Query can be done
  by providing some text or by submitting a piece of audio.
* Support for advanced queries combining content analysis features and other
  metadata (tags, etc) including filters and group-by options.
* Support for duplication detection. It helps in finding duplicate entries in
  the collection.
* Helps in finding relevant audios quickly and efficiently.

Software Requirements
---------------------

* Elastic search (storage database)
* elastic-py library
* Kibana (data visualization)
* Python 2.7.x/C
* Scikit, Keras
* Coverage
* Pep8
* Pyflakes
* Sphinx (documentation)
* Python Unit-testing framework

Phase I Architecture Design
----------------------------

.. image:: images/arch


Data is pass to feeder module in json format. There are two ways for passing
data to feeder module.

* sending data(already extracted features from AcousticBrainz) directly;
* First extracting features using Essentia toolkit and the produced json files
  are passed to feeder.

Feeder parses the json files and calls the elasticsearch api(s) to create
indexes for the features. Further PeragroClient API(s) provides method for
quering(search) the indexes. Kibana is used to visualize, analyze and search
the data in GUI.


The outline of the work
------------------------

Work was divided into the following steps:

* Requirements gathering
* dataset creation
* feature extraction
* building index
* building client search api(s)
* visualization of indexed data


Dataset creation
****************

There are two ways of feeding data to the system which has been tested.

* AcousticBrainz data
* created dataset

**AcousticBrainz data**: It is a dump of 10+ GB of highlevel data and 40+ GB of
lowlevel data.

It can be downloaded from http://acousticbrainz.org/download

This dataset contains already extracted features which was good to test initial
build of the system. Huge amount of data provided a good base for testing
scalibity and performance of the system.

**created dataset**: This dataset was created by downloading audio from
`freesound.org` by doing tagsearch using the `freesound-python` api(s). It also
contains the initial set of meta data provided by the freesound.

It has around 6 GB of data. Each audio file is of duration 10 second.

This dataset is used for testing is phase I as well as in further phases.
Feature extraction is done on this dataset and then the features were indexed.

To know more about how this data was created: see Audio dataset creation
section in the content.


Feature extraction
*******************

Features are extracted from the audio files using the binaries provided by
essentia toolkit.

These binaries are placed in the `src/bin` directory.

`extractor` module contains the `FeatureExtractor` class which is responsible
for providing methods for extracting features from audio files.


`Input`: Input is audio files or directory containing audio files.

`output`: extracted features written to json files.

A demo code:

.. code-block:: python

    from extractor import FeatureExtractor

    type_ = "gen"
    fe = FeatureExtractor(type_)

    # extract features for single audio
    fe.extract(inputFilePath, outFilePath)

    # extract features for multiple audio with extension ext inside source_dir
    # and write features files to output_dir
    fe.extract(source_dir, output_dir, ext)


For more details visit API(s) section in the content.


Building Index
***************

`feed` module is built for building index. It provides `Feeder` class that has
different methods for feeding data to elasticsearch index. For details about
the api(s) provided, please refer to API(s) documentation of Peragro AT in the
content section

Also, look at the example code provided in `examples/demo.py` to know how these
api(s) are used.


A demo code:

.. code-block:: python

    from feed import Feeder

    f = Feeder()

    # feed single feature file for index creation
    f.feed(jsonFile, cont_id, iname='audio_index', doc_type='audio')

    # feed all features file in a directory
    f.feedAll(jsonDir, iname='audio_index', doc_type='audio')


Making Search API(s)
*********************

Search API(s) are provided by the `PeragroClient` class in the `peragro` module.
Currently it provides `id-based` and `text based` search. In later stage it
will provide similarity measure, filter search, audio-fingerprint etc.

Look at the API(s) documentation in the content section for more details. Also,
view `examples/demo.py` and `examples/README` to understand how it's used.


Visualization of Indexed data
******************************

Indexed data can be visualized, analysed and also queried using Kibana GUI.
You need to install Kibana and then point the index-name to kibana indexed
pattern.

Details to do this can be found at `Audio Data Visualization/Analytics Using
Kibana` section of the content.


Steps for Demo
--------------

Created dataset(freefield) will be used as our audio database.

Following are the operations performed.

* create dataset/ Download dataset (I have given dropbox link below)
* Run feature extractor
* Run index builder
* make queries

Download dataset
****************

Download dataset form here
https://www.dropbox.com/s/zvwf2u69zfvi2yj/my_data.tar.gz?dl=0

Feature extraction
*******************

This is done using `FeatureExtractor` class provided in `extractor` module

Index builder
*************

Done by using `Feeder` class provided in `feed` module

Making queries
**************

Done by using `PeragroClient` module provided in `peragro` module.

Run demo
**********

`main.py` file is provided in the `src` directory which does all of the above
steps.

Type the following command under `src` directory:

.. code-block:: bash
    $ python main.py <source_dir>


Where `source_dir` is the path of `created dataset`.

.. note::

    After downloading the dataset extract the files.

.. code-block:: bash
    $ tar -xvf my_data

similarly extract the files inside `my_data` too.

Once the index is created by `main.py` you can visualize the data by Kibana
by pointing your browser to:

.. code-block:: bash

    $ http://localhost:5601


make sure that kibana is installed before doing above otherwise, go through the
topic 'Audio data visualization' in the content to install and learn about
kibana.



Contents:

.. toctree::
   :maxdepth: 2

   install
   dataset
   visualize
   code
   source_code

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

