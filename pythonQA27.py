x = int(input("enter the value of x: "))
y = int(input("enter the value of y: "))

z = int(input("enter the value of z : "))

def sumthree(x,y,z):
    if x ==y or y ==z or x==z:
        sum = 0
    else:
        sum = x+y+z
    return sum
print(sumthree(x,y,z))
        