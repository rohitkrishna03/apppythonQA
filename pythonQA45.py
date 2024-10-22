# Write a Python program to check whether multiple variables have the same value.
x = input("enter the value of x : ")
y = input("enter the value of y : ")
z = input("enter the value of z : ")
def samevalue(x,y,z):
    if x==y==z:
        return "all have same value"
    else:
        return "values dont match"
    
print(samevalue(x,y,z))