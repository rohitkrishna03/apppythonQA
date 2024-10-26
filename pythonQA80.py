def not_denom(n):
    Q =[500,200,100,50,20,10]
    x = 0
    for i in range(6):
        q =Q[i]
        x +=int(n/q)
        n =int(n%q)
    if n >0:
        x =-1
    return x
print(not_denom(10000))