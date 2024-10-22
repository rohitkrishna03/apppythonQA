# 
# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def test_data(num):
    if len(num) ==len(set(num)):
        return True
    else:
        return False
print(test_data([1,2,3,4,5,6,7]))
print(test_data([1,2,3,4,5,5,7]))
print(test_data([1,1,3,4,5,6,7]))

