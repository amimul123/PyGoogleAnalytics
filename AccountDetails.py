class AccountGA:
    def  __init__(self, brand):
        self.accounts = []
        self.startDate =''
        self.endDate = ''
        self.brand = brand
        self.fileName = ''
        print("class object")

    def set_dateRange(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate

    def set_file_name(self, fileName):
        self.fileName = fileName
    
    # view_id from google analytics account
    # exchange_rate for euro 
    def set_credential(self):
        accounts = [
            {'country': 'DE', 'currency': 'EURO','exchange_rate': 1, 'view_id': '0000000'},
            {'country': 'AT', 'currency': 'EURO','exchange_rate': 1, 'view_id': '0000000'},
            {'country': 'CH', 'currency': 'CHF','exchange_rate': 0.95, 'view_id': '0000000'},
            {'country': 'IT', 'currency': 'EURO','exchange_rate': 1, 'view_id': '0000000'},
            {'country': 'ES', 'currency': 'EURO','exchange_rate': 1, 'view_id': '0000000'},
            {'country': 'FR', 'currency': 'EURO','exchange_rate': 1, 'view_id': '0000000'},
            {'country': 'PT', 'currency': 'EURO','exchange_rate': 1, 'view_id': '0000000'},
            {'country': 'HU', 'currency': 'EURO','exchange_rate': 1, 'view_id': '0000000'},
            {'country': 'SE', 'currency': 'SEK','exchange_rate': 0.095, 'view_id': '0000000'},
            {'country': 'International', 'currency': 'USD','exchange_rate': 0.88, 'view_id': '000000'},
        ]
        self.accounts = accounts
            
    def get_credential(self):
        return self.accounts

    def get_dateRange(self):
        return self.startDate, self.endDate

    def get_file_name(self):
        return self.fileName
    
    def get_brand(self):
        return self.brand