import transactions
import user
import stocks
import read_crypto_data
import get_crypto_data
import wallet_carrier


# Create a stock market
nsd = stocks.Stock_Market('USA')
#nsd.getStockAttributes('TSLA').printStock()

# Create two users
kypr = user.User('kypr','kyprianosmantis@gmail.com', '123456')
kypr2 = user.User('kypr2','kyprianosmantis@gmail.com', '123456')

# Create carriers (and add them to the Carrier Dictionary)
wallet_carrier.Carrier('National Bank of Greece')
wallet_carrier.Carrier('Piraeus Bank')
wallet_carrier.Carrier('PayPal')

# Create new accounts and add them to the 
# corresponding carrier's accounts dictionary
tempAcc = wallet_carrier.Account(1234567890, 'Qwerty!@34', 'National Bank of Greece', 1000)
wallet_carrier.carrierDictionary[tempAcc.carrierName].accounts[tempAcc.ID] = tempAcc
tempAcc = wallet_carrier.Account(4567890123, 'Qwerty!@34', 'Piraeus Bank', 2500)
wallet_carrier.carrierDictionary[tempAcc.carrierName].accounts[tempAcc.ID] = tempAcc
tempAcc = wallet_carrier.Account('kiprianosmantis@gmail.com', 'Qwerty!@34', 'PayPal', 4000)
wallet_carrier.carrierDictionary[tempAcc.carrierName].accounts[tempAcc.ID] = tempAcc

# Add payment methods to wallet
kypr.wallet.addPaymentMethod('National Bank of Greece',(1234567890, 'Qwerty!@34'))
kypr.wallet.addPaymentMethod('Piraeus Bank',(4567890123, 'Qwerty!@34'))
kypr.wallet.addPaymentMethod('PayPal',('kiprianosmantis@gmail.com', 'Qwerty!@34'))

#wallet_carrier.printAllAccountsInAllCarriers()
# Buy a stock
kypr.getUserTransactions()
kypr.buy({nsd.getStockAttributes('TSLA'):(2, False)})
kypr.wallet.printPaymentMethods()

#kypr.tradingHistory.append(transactions.Transaction(kypr, 10, False))