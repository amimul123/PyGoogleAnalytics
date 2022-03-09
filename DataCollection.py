from datetime import datetime
import AccountDetails as acd
import GoogleAnalytics as pyGa

yearMonth = datetime.now().strftime("%Y-%m")

obj = acd.AccountGA('your brand name')
obj.set_dateRange('2022-01-01','2022-01-31')
obj.set_credential()
# {brand}_GA_2022-01.csv, where the data will be stored
obj.set_file_name(obj.get_brand() + "_GA_" + yearMonth + ".csv")
#print(obj.get_credential())

# data collection for all countries
for account in obj.get_credential():
    startDate, endDate = obj.get_dateRange()
    fileName = obj.get_file_name()
    pyGa.get_ga_data(account, startDate, endDate, fileName)
    
# end
