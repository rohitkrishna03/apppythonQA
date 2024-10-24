# # # Example: CreditCard Class
# # class CreditCard:
# # 2 ”””A consumer credit card.”””
# # 3
# # 4 def init (self, customer, bank, acnt, limit):
# # 5 ”””Create a new credit card instance.
# # 6
# # 7 The initial balance is zero.
# # 8
# # 9 customer the name of the customer (e.g., John Bowman )
# # 10 bank the name of the bank (e.g., California Savings )
# # 11 acnt the acount identifier (e.g., 5391 0375 9387 5309 )
# # 12 limit credit limit (measured in dollars)
# # 13 ”””
# # 14 self. customer = customer
# # 15 self. bank = bank
# # 16 self. account = acnt
# # 17 self. limit = limit
# # 18 self. balance = 0
# # 19
# # 20 def get customer(self):
# # 21 ”””Return name of the customer.”””
# # 22 return self. customer
# # 23
# # 24 def get bank(self):
# # 25 ”””Return the bank s name.”””
# # 26 return self. bank
# # 27
# # 28 def get account(self):
# # 29 ”””Return the card identifying number (typically stored as a string).”””
# # 30 return self. account
# # 31
# # 32 def get limit(self):
# # 33 ”””Return current credit limit.”””
# # 34 return self. limit
# # 35
# # 36 def get balance(self):
# # 37 ”””Return current balance.”””
# # # 38 return self. balance
# def charge(self, price):
# 40 ”””Charge given price to the card, assuming sufficient credit limit.
# 41
# 42 Return True if charge was processed; False if charge was denied.
# 43 ”””
# 44 if price + self. balance > self. limit: # if charge would exceed limit,
# 45 return False # cannot accept charge
# 46 else:
# 47 self. balance += price
# 48 return True
# 49
# 50 def make payment(self, amount):
# 51 ”””Process customer payment that reduces balance.”””
# 52 self. balance −= amount