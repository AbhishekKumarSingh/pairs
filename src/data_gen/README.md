# Audio dataset creation

Dataset is created using the scripts in the `data_gen` directoy. Based on tag search audio is searched and downloaded from the [freesound](http://freesound.org) along with their metadata. And then produced 10-second snippets from each one, as long as they matches the requirements. Data were also sampled from the downloaded set.

### get_sound module:

This module is responsible for getting sound and their metadata based on tagsearch results from freesound.org. Metadata is stored in json file format. File format is like metadata for audio having id as `12345` has its metadata stored in `12345.json` file.

### snippetmaker module:

This module is responsible for generating 10-second snippets from each one of the downloaded audios.

## Installing dependencies

1. make virtual environment inside `data_gen` directory:
        
        $ virtualenv env

2. activate virtual environment

        $ source env/bin/activate

3. install requirements form `requirements.txt`

        $ pip install requirements.txt

4. clone freesound python bindings `freesound-python`

        $ git clone https://github.com/danstowell/freesound-python
        
5. install `freesound-python` inside virtual environment

        # when your virtual environment is active
        $ python setup.py install
        
## Procedure to run the modules

`Note`: module get_sound.py performs heavy hits on freesound server. please take permission from freesound before hand.

#### Get freesound api token

To authenticate API calls with the token strategy you’ll need to create a Freesound account (if you don’t have one yet!) and request a new API credential by visiting http://www.freesound.org/apiv2/apply. In this page you’ll see a table with all API credentials you have requested plus some other information. You should use the keys in ‘Client secret/Api key’ column, which are long alphanumeric strings. You should get a different API key for every application you develop.

#### Add freesound client api key

replace null string with acutal client_api_key in `local_data.py`

    freesound_api_key = <client_api_key>

### Run modules

    $ python get_sound.py
    $ python snippetmaker.py

