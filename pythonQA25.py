# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

x = int(input("enter the value of x : "))
y = int(input("enter the value of y : "))
def sumdiff(x,y):
    if x==y or abs(x-y) ==5  or (x+y) ==5 :
        return True
    else:
        return False
    
print(sumdiff(x,y))
        