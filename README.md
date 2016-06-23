# Peragro Audio Information Retrieval System (PAIRS)
----
## Purpose:
“Search, and you will find”

Implementation of an audio search system for Peragro. An Audio Information Retrieval(AIR)
system that would provide client API(s) for audio search and information retrieval.
Search will be based on annotated text/descriptions or tags/labels associated
with an audio as well as on low and high level features. Focus is to implement
an AIR system that provides text based and content based search. Users would be
able to perform query through the provided client API(s) and will get list of relevant audios in return.

## Dependency requirements

* Elasticsearch
* elasticsearch-py
* sphinx
* Kibana

## Installing dependencies
**Install elasticsearch**

First, you need to install OpenJDK

    $ sudo apt-get install openjdk-7-jre

To verify your JRE is installed and can be used, run the command:

    $ java -version

The result should look like this:

    Output of java -version
    java version "1.7.0_79"
    OpenJDK Runtime Environment (IcedTea 2.5.6) (7u79-2.5.6-0ubuntu1.14.04.1)
    OpenJDK 64-Bit Server VM (build 24.79-b02, mixed mode)


Installing Java 8

    $ sudo add-apt-repository -y ppa:webupd8team/java
    $ sudo apt-get update

Install the latest stable version of Oracle Java 8 with this command (and accept the license agreement that pops up):

    $ sudo apt-get -y install oracle-java8-installer

verify it is installed:

    $ java -version

**Downloading and Installing Elasticsearch**

    $ wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.2.deb
    $ sudo dpkg -i elasticsearch-1.7.2.deb

To make sure Elasticsearch starts and stops automatically, add its init script to the default runlevels with the command:

    $ sudo update-rc.d elasticsearch defaults

start Elasticsearch

    $ sudo service elasticsearch start

For more detailed info on configuration you can follow the tutorial at: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-14-04

#### Alternate option


Use script to downlaod and install elasticsearch:

run the script at: https://gist.github.com/ricardo-rossi/8265589463915837429d


**Install sphinx**

    $ sudo apt-get install sphinx


**Install elasticsearch-py**

    $ pip install elasticsearch>=2.3.0


**Install and start Kibana**

Installing kibana with apt-get

1. Download and install the Public Signing Key:

         $ wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

2. Add the repository definition to your /etc/apt/sources.list.d/kibana.list file:

         $ echo "deb http://packages.elastic.co/kibana/4.5/debian stable main" | sudo tee -a /etc/apt/sources.list

3. Run apt-get update and the repository is ready for use. Install Kibana with the following command:

         $ sudo apt-get update && sudo apt-get install kibana

4. Configure Kibana to automatically start during bootup. If your distribution is using the System V version of init, run the following command:

         $ sudo update-rc.d kibana defaults 95 10

5. start kibana

         $ sudo service kibana start

That’s it! Kibana is now running on port 5601. You can access the kibana UI by pointing your browser to:
http://localhost:5601

## Buidling docs

Inside `doc` directory run

    $ make html
    
Docs is also online at: http://pairs.readthedocs.io/en/latest/ 
