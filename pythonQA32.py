# Write a Python program to get the execution time of a Python method.



import time

def sum_of_n_num(n):
    
    start_time =time.time()
    
    s=0
    
    for i in range(1, n+1):
        s =s+i
        
    end_time =time.time()
    
    return s,end_time -start_time
n=5
print("\nTime to sum of 1 to", n, "and required time to calculate is:", sum_of_n_num(n))

