# Write a Python program to find the median among three given numbers.

x = int(input("enter the value of x: "))
y = int(input("enter the value of y: "))
z = int(input("enter the value of z: "))
print("median of all the three numbers")

if y<x and x<z:
    print(x)
elif z<x and x<y:
    print(x)
elif z<y and y<x:
    print(y)
elif x<y and y<z:
    print(y)
elif y<z and z<x:
    print(z)
elif x<z and z<y:
    print(z)


