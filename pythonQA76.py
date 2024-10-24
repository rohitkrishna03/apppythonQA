# Python: Find the value of n where n degrees of number 2 are written sequentially in a line without spaces

def ndegree(n):
    ans = True
    n, tempn, i =2,2,2
    # here initializing all the values of n,temp,i to 2
    while ans:
        if str(tempn) in n:
            i += 1 #increment with i 
            tempn = pow(n,i)
        else:
            ans = False
    return i-1
print(ndegree("2481632"))
        
            
    