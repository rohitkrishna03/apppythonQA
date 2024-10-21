# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user

num = int(input("enter the anu number to know if ot is even or odd : "))
def evenOdd(num):
    if num%2 ==0:
        return "this is even number"
    else:
        return "this is odd number"
    
print(evenOdd(num))