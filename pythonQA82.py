def eveodd(n):
    x =len([i for i in range(1, n+1) if not n%i])
    return x
print(eveodd(24))