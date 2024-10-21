# Write a Python program to empty a variable without destroying it.

# type() returns the type of an object, which when called produces an 'empty' new value.



def empty_value(list):
    
    return [type(i)() for i in list]

list=["python",{"x":12},[10,20],(2,3),200]
print(empty_value(list))