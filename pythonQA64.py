# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.r

def count_div(n):
    if n<=2:
        return "enter the greater number than 2"
    count =0
    while n>= 2:
        n/=2
        count +=1
    return count
try:
    number = int(input("enter a positive/greater number than 2 : "))
    result = count_div(number)
    print(f"the number is divided by 2 : {result}")
except ValueError:
    print("enter the valid integer")
    
    
    # Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.
# amount = int(input(" enter the amount charged"))
def make_change(charged, given):
     denominations = {
        "hundred dollar bills": 10000,
        "fifty dollar bills": 5000,
        "twenty dollar bills": 2000,
        "ten dollar bills": 1000,
        "five dollar bills": 500,
        "one dollar bills": 100,
        "quarters": 25,
        "dimes": 10,
        "nickels": 5,
        "pennies": 1
    }
     changed_amount = given-charged
     if changed_amount<0:
         return "insufficient amount given"
     change ={}
     change_amount_cents = int(changed_amount *100)
     
     for name, value in denominations.items():
         count = change_amount_cents // value
         if count >0:
             change[name] =count
             change_amount_cents -= count*value
     return change
try:
    changed_amount =float(input("enter the amount changed: $: "))
    given_amount = float(input("enter the given amount : $"))
    change = make_change(changed_amount, given_amount)
    
    if isinstance(change, str):
        print(change)
        
    else:
        print("change to give back : ")
        for denomination, count in change.items():
            print(f"{count} {denomination}")
            
except ValueError:
    print("please enter valid monetary amounts.")
    
    