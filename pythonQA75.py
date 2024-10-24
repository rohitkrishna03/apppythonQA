# Write a Python program to find the number of zeros at the end of a factorial of a given positive number.

def factorzero(n):
    
    x =n//5
    y=x
    
    while x>0:
        x/=5
        y +=int(x)
    return y
print(factorzero(45678))