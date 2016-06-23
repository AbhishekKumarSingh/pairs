Installation Instruction for PAIRS
==================================

Dependency requirements
-----------------------

* Elasticsearch
* elasticsearch-py
* sphinx
* Kibana

Installing dependencies
------------------------

Install elasticsearch
*********************

First, you need to install OpenJDK


.. code-block:: bash

    $ sudo apt-get install openjdk-7-jre


To verify your JRE is installed and can be used, run the command:


.. code-block:: bash

    $ java -version


The result should look like this:


.. code-block:: bash

    Output of java -version
    java version "1.7.0_79"
    OpenJDK Runtime Environment (IcedTea 2.5.6) (7u79-2.5.6-0ubuntu1.14.04.1)
    OpenJDK 64-Bit Server VM (build 24.79-b02, mixed mode)


**Installing Java 8**


.. code-block:: bash

    $ sudo add-apt-repository -y ppa:webupd8team/java
    $ sudo apt-get update


Install the latest stable version of Oracle Java 8 with this command (and accept the license agreement that pops up):


.. code-block:: bash

    $ sudo apt-get -y install oracle-java8-installer


verify it is installed:


.. code-block:: bash

    $ java -version


**Downloading and Installing Elasticsearch**


.. code-block:: bash

    $ wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.2.deb
    $ sudo dpkg -i elasticsearch-1.7.2.deb


To make sure Elasticsearch starts and stops automatically, add its init script to the default runlevels with the command:


.. code-block:: bash

    $ sudo update-rc.d elasticsearch defaults


start Elasticsearch


.. code-block:: bash

    $ sudo service elasticsearch start


For more detailed info on configuration you can follow the tutorial at: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-14-04

Alternate option
*******************

Use script to downlaod and install elasticsearch:

run the script at: https://gist.github.com/ricardo-rossi/8265589463915837429d


Install sphinx
***************


.. code-block:: bash

    $ sudo apt-get install sphinx


Install elasticsearch.py
**************************


.. code-block:: bash

    $ pip install elasticsearch>=2.3.0


Install and start Kibana
*************************

Installing kibana with apt-get

1. Download and install the Public Signing Key:


   .. code-block:: bash

        $ wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -


2. Add the repository definition to your /etc/apt/sources.list.d/kibana.list file:


   .. code-block:: bash

        $ echo "deb http://packages.elastic.co/kibana/4.5/debian stable main" | sudo tee -a /etc/apt/sources.list


3. Run apt-get update and the repository is ready for use. Install Kibana with the following command:


   .. code-block:: bash

        $ sudo apt-get update && sudo apt-get install kibana


4. Configure Kibana to automatically start during bootup. If your distribution is using the System V version of init, run the following command:


   .. code-block:: bash

        $ sudo update-rc.d kibana defaults 95 10


5. start kibana


   .. code-block:: bash

        $ sudo service kibana start


That’s it! Kibana is now running on port 5601. You can access the kibana UI by pointing your browser to:

.. code-block:: bash

    http://localhost:5601
