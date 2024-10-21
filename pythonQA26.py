# Write a Python program to add two objects if both objects are integers.

x =input("enter the value of x : ")
y= input("enter the value of y : ")


def add_num(x,y):
    
    if not  (isinstance(x, int) and isinstance(y, int)):
      return "numbers must be integer"
    else:
      return a+b
    
print(add_num(x,y))
    