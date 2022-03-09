# PyGoogleAnalytics
Fetch data from Google Analytics through Python

# Installation
pip install virtualenv <br/>
virtualenv <your-env-name>  <br/>
<your-env-name>\Scripts\activate  <br/>
<your-env-name>\Scripts\pip.exe install google-api-python-client  <br/>
pip install --upgrade google-api-python-client  <br/>
pip install --upgrade oauth2client  <br/>

# Setup
Add your google credential JSON file location to the <b>GoogleAnalytics.py</b> file <br/>
  KEY_FILE_LOCATION = 'your json file' <br/>
Add your google analytics <b>view_id</b> to the <b>AccountDetails.py</b> file  <br/>
  'country': 'DE', 'currency': 'EURO','exchange_rate': 1, <b>'view_id'</b>: '0000000' <br/>
Run the script, python .\DataCollection.py
