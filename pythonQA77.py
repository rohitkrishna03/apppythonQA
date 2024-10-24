# Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.

def permutation(nums):
    result_perms =[[]]
    for n in nums:
        new_perms =[]
        
        for perms in result_perms:
            for i in range(len(perms)+1):
                new_perms.append(perms[:i] +[n] +perms[i:])
                result_perms = new_perms
    return result_perms
my_nums = [1,2,3]
print("orginal collection:" ,my_nums)
print("collected from nums: " ,permutation(my_nums))
    
                