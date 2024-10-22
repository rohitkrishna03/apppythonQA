# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# Note: Do not use built-in functions.

def max_min(data):
    max =data[0]
    min =data[0]
    
    for num in data:
        if num > max:
            max = num
        elif num < min:
            min = num
            
    return max,min
print(max_min([0,10,20,12,34,87,123,4,98,0,6]))

        
    