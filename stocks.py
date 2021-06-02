import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

class Stock():
    def __init__(self, name, symbol, dailyStockValues):
        self.symbol = symbol
        self.name = name
        self.dailyStockValues = dailyStockValues

    def printStock(self, formatted=True):
        print('--Stock information--\nName:',self.name, '\nSymbol:', self.symbol,'\nDaily Data:')
        for key in self.dailyStockValues:
            if formatted==True:
                formatedMonth = '{:02d}'.format(key.month)
                formatedDay = '{:02d}'.format(key.day)
            else:
                formatedMonth = key.month
                formatedDay = key.day
            print(f"{key.year}-{formatedMonth}-{formatedDay} {self.dailyStockValues[key]}")

class Stock_Market():
    def __init__(self, country):
        self.country = country
        self.market_indexes = []
        self.stocks = {}
        self.getAllStocksData()
    
    def getStockDataFromAPI(self, name, symbol, start, end):
        dailyStockValues = {}
        style.use('ggplot')
        df = web.DataReader(symbol, 'yahoo', start, end)
        dailyStockValues = df.to_dict(orient='index')
        tempStock = Stock(name, symbol, dailyStockValues)
        self.stocks[symbol] = tempStock

    def getAllStocksData(self):
        tsla    = ['Tesla Inc', 'TSLA']
        amd     = ['Advanced Micro Devices, Inc.', 'AMD']
        googl   = ['Alphabet Inc.','GOOGL']
        fb      = ['Facebook, Inc.','FB']
        zm      = ['Zoom Video Communications, Inc.','ZM']
        czr     = ['Caesars Entertainment Inc','CZR']
        cat     = ['Caterpillar Inc.','CAT']
        stocksToGet = [tsla, amd, googl, fb, zm, czr, cat]
        
        for aStock in stocksToGet:
            tmp = self.getStockDataFromAPI(aStock[0], aStock[1], dt.datetime(2020, 1, 1), dt.datetime.now())

    def getStockAttributes(self, symbol):
        return self.stocks[symbol]

    def printAllStockNames(self):
        for s in self.stocks:
            print(s, self.stocks[s].name)

nsd = Stock_Market('USA')
nsd.getStockAttributes('TSLA').printStock()