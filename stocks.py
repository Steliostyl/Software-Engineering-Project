import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

class Stock():
    def __init__(self, name, symbol, dailyValues):
        self.symbol = symbol
        self.name = name
        self.dailyValues = dailyValues

    def printStock(self, formatted=True):
        print('--Stock information--\nName:',self.name, '\nSymbol:', self.symbol,'\nDaily Data:')
        for key in self.dailyValues:
            if formatted==True:
                formatedMonth = '{:02d}'.format(key.month)
                formatedDay = '{:02d}'.format(key.day)
            else:
                formatedMonth = key.month
                formatedDay = key.day
            print(f"{key.year}-{formatedMonth}-{formatedDay} {self.dailyValues[key]}")

class Stock_Market():
    def __init__(self, country):
        self.country = country
        self.market_indexes = []
        self.stocks = {}
        self.getAllStocksData()
    
    def dfToDictCustom(self, df, tempDict):
        finalDict = {}
        #print(tempDict)
        for key in tempDict:
            #print("Key: ", key)
            #print(tempDict)
            finalDict[dt.date(key.year, key.month, key.day)] = tempDict[key]
        #print(finalDict)
        return finalDict

    def getStockDataFromAPI(self, name, symbol, start, end):
        dailyValues = {}
        style.use('ggplot')
        df = web.DataReader(symbol, 'yahoo', start, end)
        #df.index = pd.to_datetime(df.index).date()
        #print(df.index, type(df.index))
        tempDict = df.to_dict(orient='index')
        finaldict = self.dfToDictCustom(df, tempDict)
        #print(finaldict)
        #df.reset_index(inplace=True,drop=False)
        #df['Date'] = pd.to_datetime(df['Date']).dt.date
        #print(df['Date'][0],type(df['Date'][0]))

        tempStock = Stock(name, symbol, finaldict)
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
            tmp = self.getStockDataFromAPI(aStock[0], aStock[1], dt.datetime(2021, 6, 1), dt.datetime.now())

    def getStockAttributes(self, symbol):
        return self.stocks[symbol]

    def printAllStockNames(self):
        for s in self.stocks:
            print(s, self.stocks[s].name)

#nsd = Stock_Market('USA')
##nsd.getStockAttributes('TSLA').printStock()
#print(dt.datetime(2020,1,2))
#print(nsd.getStockAttributes('TSLA').dailyValues[dt.datetime(2020,1,2)]['Close'])