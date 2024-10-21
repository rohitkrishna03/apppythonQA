# Write a Python program to sort three integers without using conditional statements and loops.

x =int(input("enter the value of x: "))
y =int(input("enter the value of y: "))
z =int(input("enter the value of z: "))

a1 =min(x,y,z)
a2 =max(x,y,z)

a3 =(x+y+z)-a1-a2

print("the numbers in sorted order :" ,a1,a3,a2)
