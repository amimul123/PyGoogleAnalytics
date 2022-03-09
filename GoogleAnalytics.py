import locale
import os
import pandas as pd
import numpy as np
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'your json file'


def initialize_analyticsreporting():
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)
  return analytics

def get_report(analytics, view_id, startDate, endDate):

  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': view_id,
          'pageSize': 100000,
          'dateRanges': [{'startDate': startDate, 'endDate': endDate}],
          'metrics': [{'expression': 'ga:sessions'},
            {'expression': 'ga:newUsers'},
            {'expression': 'ga:bounceRate'},
            {'expression': 'ga:transactions'},
            {'expression': 'ga:transactionRevenue'},
            {'expression': 'ga:uniqueEvents'},
            {'expression': 'ga:transactionsPerSession'},
            {'expression': 'ga:revenuePerTransaction'},
            #{'expression': 'ga:adCost'},
          ],
          'dimensions': [
            #{'name': 'ga:country'},
            {'name': 'ga:date'},
            {'name': 'ga:year'},
            {'name': 'ga:month'},
            {'name': 'ga:eventCategory'},
          ],
          'dimensionFilterClauses': [
            {
              "filters": [
                {
                  "dimensionName": "ga:eventCategory",
                  "operator": "PARTIAL",
                  "expressions": ["Login"]
                }
              ]
            }
          ],
        }]
      }
  ).execute()

def print_response_test(response):
  print(response)
  pagetoken = response.get("reports")[0].get('nextPageToken')
  print(pagetoken)

def print_response_all(response, currency, exchangeRate):

  # print(type(response))
  # print(response)
  report = response.get('reports',[])
  dimHeaders = report[0].get('columnHeader',{}).get('dimensions',[])
  metricHeaders = report[0].get('columnHeader',{}).get('metricHeader',{}).get('metricHeaderEntries',[])
  tabHeader = dimHeaders
  metricTypes = []
  for metHead in metricHeaders:
    tabHeader.append(metHead.get('name'))
    metricTypes.append(metHead.get('type'))

  #print(tabHeader)

  tabBody=[]
  for row in  report[0].get('data',{}).get('rows',[]):
    # dimentions value
    tempRow = row.get('dimensions',[])
    for metVal in row.get('metrics',[]):
      # matrics values
      temMetricValues = metVal.get('values',[])
      tempRow = tempRow +  format_data(temMetricValues, metricTypes, currency, exchangeRate) # temMetricValues
    #print(tempRow)
    tabBody.append(tempRow)
  return tabHeader, tabBody
  
  # full dataset
  # print(tabBody)

def format_data(data, dataTypes, reqCurrency, exchangeRate):
  for idx, val in enumerate(data):
    if dataTypes[idx] == "INTEGER":
      data[idx] = int(data[idx])
    elif dataTypes[idx] == "PERCENT":
      data[idx] =  data[idx][:data[idx].find(".")+3].replace(".",",") + "%" # round(float(data[idx]),2) +'%'
    elif dataTypes[idx] == "CURRENCY":
      data[idx] = currency_format(float(data[idx]),reqCurrency, exchangeRate)
  return data      

def currency_format(val, reqCurrency, exchangeRate):
  """if reqCurrency == "EURO":
    val = val * 1
  elif reqCurrency == "CHF":
    val = val * 0.95
  elif reqCurrency == "SEK":
    val = val * 0.095
  elif reqCurrency == "USD":
    val = val * 0.88
  """
  val = val * exchangeRate  
  locale.setlocale( locale.LC_ALL, 'de_DE.UTF-8' )
  newVal = locale.currency(round(val,2), grouping=True )
  return newVal

def get_ga_data(account, startDate, endDate, filePath):
  view_id = account['view_id']
  currency = account['currency']
  exchangeRate = account['exchange_rate']

  analytics = initialize_analyticsreporting()
  response = get_report(analytics, view_id, startDate, endDate)
  tabHeader, tabBody = print_response_all(response, currency, exchangeRate)
  df_all = pd.DataFrame(tabBody,
                 columns=tabHeader)
  df_all.set_index(df_all['ga:date'], inplace=True)
 
  df_all.drop(columns=['ga:date'], inplace=True)
  df_all.insert(loc=0, column='country', value=account['country'])
  #print(df_all)
  df_all.to_csv(path_or_buf=filePath, sep=";", index=False, mode="a", header=not os.path.exists(filePath))

if __name__ == '__main__':
  get_ga_data()
