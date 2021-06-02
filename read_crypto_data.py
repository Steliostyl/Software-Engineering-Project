import pandas as pd
import get_crypto_data as gcd
import csv
from datetime import datetime
from matplotlib import style

from_symbol = 'BTC'
to_symbol = 'USD'
exchange = 'Bitstamp'
datetime_interval = 'day'
name = 'Bitcoin'

class Crypto_Coin():
    def __init__(self, name, symbol, dailyCryptoValues):
        self.symbol = symbol
        self.name = name
        self.dailyCryptoValues = dailyCryptoValues

    def filterCryptoData(self, startingDate):
        tempDailyCryptoValues = {}
        for val in self.dailyCryptoValues:
            #print(type(val))
            if val>=startingDate :
                tempDailyCryptoValues[val] = self.dailyCryptoValues[val]
        return Crypto_Coin(self.name, self.symbol, tempDailyCryptoValues)

    def printCrypto(self, formatted=True):
        print('--Crypto Coin information--\nName:',self.name, '\nSymbol:', self.symbol,'\nDaily Data:')
        for key in self.dailyCryptoValues:
            if formatted==True:
                formatedMonth = '{:02d}'.format(key.month)
                formatedDay = '{:02d}'.format(key.day)
            else:
                formatedMonth = key.month
                formatedDay = key.day
            print(f"{key.year}-{formatedMonth}-{formatedDay} {self.dailyCryptoValues[key]}")

class Crypto_Market():
    def __init__(self, country):
        self.country = country
        self.market_indexes = []
        self.cryptoCoins = {}
        self.getAllCryptoData()
    
    def createDict(self, filename):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            cryptocoinDict = {}
            for row in csv_reader:
                #if line_count == 0:
                #    print(f'Column names are {", ".join(row)}')
                #    line_count += 1
                tempDailyCryptoValues = {}
                tempDailyCryptoValues['low'] = row['low']
                tempDailyCryptoValues['high'] = row['high']
                tempDailyCryptoValues['open'] = row['open']
                tempDailyCryptoValues['close'] = row['close']
                tempDailyCryptoValues['volumefrom'] = row['volumefrom']
                tempDailyCryptoValues['volumeto'] = row['volumeto']
                #Convert row['datetime'] from string to datetime
                cryptocoinDict[datetime.strptime(row['datetime'], '%Y-%m-%d')] = tempDailyCryptoValues
                line_count += 1
        #print(f'Processed {line_count} lines.')
        cryptocoin = Crypto_Coin(name, from_symbol, cryptocoinDict)
        return cryptocoin

    def getAllCryptoData(self):
        tempfilename = gcd.get_filename(from_symbol, to_symbol, exchange, datetime_interval, datetime.now().date().isoformat())
        self.cryptoCoins[from_symbol] = self.createDict(tempfilename)

    def getCryptoCoinAttributes(self, symbol, startingDate):
        return self.cryptoCoins[symbol].filterCryptoData(startingDate)

    def printAllCryptoNames(self):
        for s in self.cryptoCoins:
            print(s, self.cryptoCoins[s].name, self.cryptoCoins[s].symbol)


cm = Crypto_Market('Greece')
#cm.printAllCryptoNames()
cm.getCryptoCoinAttributes('BTC', datetime(2020,1,1)).printCrypto()

#filename = gcd.get_filename(from_symbol, to_symbol, exchange, datetime_interval, datetime.now().date().isoformat())
#btc = Cryptocoin.createDict(gcd.get_filename(from_symbol, to_symbol, exchange, datetime_interval, datetime.now().date().isoformat()))
#btc.printCrypto()