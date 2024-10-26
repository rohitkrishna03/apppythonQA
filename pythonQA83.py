# Write a Python program to compute the summation of the absolute difference of all distinct pairs in a given array (non-decreasing order).

def sum_distinct(arr):
    result =0
    i=0
    while i<len(arr):
        result += i*arr[i] - (len(arr) -i-1)*arr[i]
        
        i+=1
    return result
print(sum_distinct([1,5,7]))