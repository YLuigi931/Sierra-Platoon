
'''
2. Create an `Account` class 
    which should have the following functionality:
  - A new account should be created with an `ID` 
    and an initial `balance`
  - Should have a `withdraw` method that accepts 
    a single parameter which represents the amount 
    of money that will be withdrawn. This method 
    should return the updated account balance.
  - Should have a `deposit` method that accepts a 
    single parameter which represents the amount of 
    money that will be deposited. This method should 
    return the updated account balance.
  - Should be able to access the current `balance` of 
    an account at any time.
'''
class Account:
    
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
    
    def withdraw(self, money):
        try:
            if money > self.balance:
                print('Insufficient Funds')
                return
            else:
                print('You Broke!')
                print('jk')
                self.balance -= money
                print(self.balance)
                return self.balance
        except Exception as e:
            print('==== Fail at Account Class ====')
            print(e)


test1 = Account('SOMe_ID', 500)
test1.withdraw(200)

    
        