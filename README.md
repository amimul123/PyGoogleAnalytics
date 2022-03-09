# PyGoogleAnalytics
Fetch data from Google Analytics through Python

# Installation
1. pip install virtualenv <br/>
2. virtualenv 'your-env-name'  <br/>
3. 'your-env-name'\Scripts\activate  <br/>
4. 'your-env-name'\Scripts\pip.exe install google-api-python-client  <br/>
5. pip install --upgrade google-api-python-client  <br/>
6. pip install --upgrade oauth2client  <br/>
  
# Setup
1. Add your google credential JSON file location to the <b>GoogleAnalytics.py</b> file <br/>
  KEY_FILE_LOCATION = 'your json file' <br/>
2. Add your google analytics <b>view_id</b> to the <b>AccountDetails.py</b> file  <br/>
  'country': 'DE', 'currency': 'EURO','exchange_rate': 1, <b>'view_id'</b>: '0000000' <br/>
3. Run the script, python .\DataCollection.py
