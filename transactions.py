from datetime import datetime, date
import math

def round_decimals_up(number:float, decimals:int=2):
    """
    Returns a value rounded up to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.ceil(number)

    factor = 10 ** decimals
    return math.ceil(number * factor) / factor

class Transaction():
    def __init__(self, user, itemBought, ammountBought, public):
        self.ammountBought = ammountBought
        self.itemBought = itemBought
        self.public = public
        self.ID = len(user.tradingHistory)
        #self.price = itemBought.dailyValues[datetime.now().date().isoformat()]['Close']
        itemBought.printStock()
        self.price = itemBought.dailyValues[date(2021, 6, 1)]['Close']
        self.payment = None
        self.dateTime = datetime.now()

    def printTransaction(self):
        print('Bought:',self.ammountBought)

class Payment():
    def __init__(self, user, price, paymentMethod, transactionList):
        self.price = price
        self.paymentMethod = paymentMethod # Account saved in Wallet
        #self.paymentID = len(user.tradingHistory)
        self.transactionList = transactionList
    
    def setPayment(user, pm, transactionList):
        paymentMethod = user.wallet.accounts[list(user.wallet.accounts)[pm]]
        print('Payment for buying:')
        totalSum = 0
        for transaction in transactionList:
            print(transaction.itemBought.symbol, transaction.price*transaction.ammountBought, '$')
            totalSum += transaction.price * transaction.ammountBought
            
        totalSum = round_decimals_up(totalSum)
        print('Total price:', totalSum)
        ans = paymentMethod.pay(totalSum)
        print(ans)
        if ans[0] == True:
            return Payment(user, totalSum, paymentMethod, transactionList)