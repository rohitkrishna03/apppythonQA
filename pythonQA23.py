# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

# The greatest common divisor (GCD) of two nonzero integers a and b is the greatest positive integer d such that d is a divisor of both a and b; that is, there are integers e and f such that a = de and b = df, and d is the largest such integer. The GCD of a and b is generally denoted gcd(a, b).

x = input("enter the first number: ")
y =input("enter the second  number" )
def gcd(x,y):
    gcd =1
    if x % y == 0:
       return y
    for k in range(int(y/2),0,-1):
      if x%k==0 and y%k==0:
        gcd = k
        break
    return gcd
gcd(x,y)
     

    