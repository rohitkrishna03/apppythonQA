# Write a  Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

x = int(input("enter a value of x: "))
y = int(input("enter a value of y: "))
def sumOFTwonum(x,y):
    if x+y >15 and x+y <20:
        return 20 
    else:
        return f"number is not between 15 and 20 bacause sum is" 
    
print(sumOFTwonum(x,y))

        