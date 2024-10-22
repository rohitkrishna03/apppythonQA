# Write a  Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified nber.

# Ex.: 8 = 73+63+53+43+33+23+13 = 784
n =int(input(
    'enter any single value : '
))
def sum_cubes(n):
    n -= 1
    total = 0
    
    while n>0:
        total += n * n * n
        n -= 1
    return total 
print(sum_cubes(n))
    