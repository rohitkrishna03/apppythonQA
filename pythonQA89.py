#  Modify the declaration of the first for loop in the CreditCard tests, from
# Code Fragment 2.3, so that it will eventually cause exactly one of the three
# credit cards to go over its credit limit. Which credit card is it?
class CreditCard:
    def __init__(self, customer,bank,account,limit,balance=0):
        self.customer=customer
        self.bank = bank
        self.account=account
        self.limit =limit
        self.balance=balance
        
    def charge(self, amount):
        if amount < 0:
            raise ValueError("insufficient balance")
        if self.balance + amount > self.limit:
            print(f"charge denied for ${self.customer} -exceeded limit!")
            return False
        self.balance += amount
        print(f"charged: ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

# initializing different limits

cards =[
    CreditCard("Alice","bank A","234567",500),
    CreditCard("Alice1","bank B","234568",600),
    CreditCard("Alice2","bank C","234569",700),
    CreditCard("Alice3","bank D","234561",800)
    
]

for i in range(3):
    amount_to_charge =0
    if i ==0:
        amount_to_charge=600
    elif i ==1:
        amount_to_charge=200
    else:
        amount_to_charge=300
    cards[i].charge(amount_to_charge)