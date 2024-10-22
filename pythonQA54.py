# Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values.

def odd_num(nums):
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                product = nums[i] * nums[j]
                if product &1:
                    return True
    return False
dt1 =[2,4,6,8]

print(dt1, odd_num(dt1))
