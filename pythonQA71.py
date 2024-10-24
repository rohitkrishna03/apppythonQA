# Write a  Python program to add two positive integers without using the '+' operator.

# Note: Use bitwise operations to add two numbers.
def add_without_operator(a,b):
    while b !=0:
        data = a & b
        a = a ^ b
        b= data << 1
    return a

print(add_without_operator(10,2))