from enum import Enum
import wallet_carrier
from datetime import datetime, date

def addYears(d, years):
    try:
        #Return same day of the current year        
        return d.replace(year = d.year + years)
    except ValueError:
        #If not same day, it will return other, i.e.  February 29 to March 1 etc.        
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

class Subscription_Plan():
    def __init__(self, subPlanTitle, cost, features):
        self.subPlanTitle = subPlanTitle
        self.cost = cost
        self.features = features # List of plan features
    def printSubPlan(self):
        print(self.subPlanTitle, self.cost, self.features)

class Subscription_Plan_List(Enum):
    STANDARD = Subscription_Plan('Standard', 0, ['default features'])
    ADVANCED = Subscription_Plan('Advanced', 10, ['default features','extra feature 1', 'extra feature 2'])
    PREMIUM = Subscription_Plan('Premium', 20, ['default features','extra feature 1', 'extra feature 2','extra feature 3','extra feature 4'])

class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.prefferedPM = None
        self.following = []
        self.portofolio = {} # A dictionary containing all bought stocks and crypto coins (one array for each)
        self.wallet = wallet_carrier.Wallet()
        self.subscriptionPlan = Subscription_Plan_List.STANDARD.value
        self.planExpDate = addYears(datetime.now(), 1)
        self.tradingHistory = [] # A list of transactions

    def getUserTransactions(self, filter=None):
        if filter == None:
            return self.tradingHistory
        # else:

kypr = User('kypr','kyprianosmantis@gmail.com', '123456')
kypr2 = User('kypr2','kyprianosmantis@gmail.com', '123456')

# Testing to see if the to plans are the same class object

#if kypr.subscriptionPlan is kypr2.subscriptionPlan:
#    print('True')
#    kypr.subscriptionPlan.printSubPlan()
#else:
#    print('False')