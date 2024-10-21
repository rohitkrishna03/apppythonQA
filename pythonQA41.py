# Write a Python program to compute the product of a list of integers (without using a for loop).

from functools import reduce
num =[1,23,34]


print("original list from  is:  ", num)
num_prod=reduce((lambda x,y : x*y), num)
print("the product of numbers is: ", num_prod)