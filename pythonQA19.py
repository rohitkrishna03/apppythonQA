# Write a Python program that checks whether a specified value is contained within a group of values.

value = input("enter few numbers here: ")
snum = input("enter any one number : ")

def match(value, snum):
    values=value.split()
    for val in values:
        if snum == val:
          return True
       
    return False
print(match(value,snum))