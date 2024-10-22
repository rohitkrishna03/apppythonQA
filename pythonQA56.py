# Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.
m = int(input(" enter the value of m : "))
n = int(input("enter the value of n : "))
def multiple(m,n):
    return True if m % n ==0 else False
print(multiple(m,n))