# Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter.
# R-2.6 If the parameter to the make payment method of the CreditCard class
# were a negative number, that would have the effect of raising the balance
# on the account. Revise the implementation so that it raises a ValueError if
# a negative value is sent.
# R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional fifth parameter to the constructor. The
# four-parameter constructor syntax should continue to produce an account
# with zero balance.

class CreditCard:
    def __init__(self, card_number:str, card_holder:str, expiration_date:str, cvv:str, balance:float=0.0):
        self.card_number= card_number
        self.card_holder=card_holder
        self.expiration_date=expiration_date
        self.cvv=cvv
        self.balance=balance
        
    def charge(self, amount:float):
            if not isinstance(amount,(int, float)):
                raise TypeError("amount must be a number ")
            if amount < 0:
                raise ValueError("amount must not be negative")
            
            self.balance += amount
            print(f"charged: ${amount:.2f} .new balance: ${self.balance:.2f}")
            
    def make_payment(self, amount:float):
            if not isinstance(amount,(int, float)):
                raise TypeError("enter a valid number : ")
            if amount > self.balance:
                raise ValueError(" insufficient balance in your account")
            
            self.balance -= amount
            print(f"payment made : ${amount:2.f} new balance: ${self.balance:2,f}")
try:
    card = CreditCard("123456789123" "rohit", "12/35", "111",100000000000.0)            
    card.charge(780)
    card.make_payment(1000)
    card.make_payment(-500) #this will raise an valueerror
except(ValueError,TypeError) as e:
    print(e)
    
            