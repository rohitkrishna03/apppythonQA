# Write a Python program to filter positive numbers from a list.

# Positive Numbers: Any number above zero is known as a positive number. Positive numbers are written without any sign or a '+' sign in front of them and they are counted up from zero, i.e. 1, + 2, 3, +4 etc.

nums =[-4,-7,34,1,2,4,-4,0,-12]
print("original number from the list", nums)

new_num=list(filter(lambda x:x>0, nums))
print("numbers after removing the negative numbers: ", new_num)S