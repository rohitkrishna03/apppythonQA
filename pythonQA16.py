# Write a Python program to count the number 4 in a given list.
def list_count(nums):
    count =0
    
    for num in nums:
        if num==4:
            count=count+1
    return count
print(list_count([1,2,4,3,5,4,6,4,7,4,2,3,4,8,7,4]))

