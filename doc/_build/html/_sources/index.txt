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


Contents:

.. toctree::
   :maxdepth: 2

   visualize
   code
   source_code

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

