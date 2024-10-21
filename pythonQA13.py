# Write a  Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

x = int(input("enter the value of x : "))
y = int(input("enter the value of y : "))
z = int(input("enter the value of z: "))
def ifValueEqual(x,y,z):
     sum = x+y+z
     if x==y==z:
         return (x+y+x)*3
     else:
         return sum
print(ifValueEqual(x,y,z))
