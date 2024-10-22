# Python3 code to demonstrate
# adding trailing zeros
# using format()
 
# initializing string
test_string = input("enter the valid string : ")
 
# printing original string
print("The original string : " + str(test_string))
 
# No. of zeros required
N = input("enter number of zeros required : ")
 
# using format()
# adding trailing zero
# N for number of elements, '0' for Zero, and '<' for trailing
temp = '{:<07}'
res = temp.format(test_string)
 
# print result
print("The string after adding trailing zeros : " + str(res))