# Write a  Python program to find the digits that are missing from a given mobile number.

def mobile_mis_num(n):
    all_nums =[1,2,3,4,5,6,7,8,9,0]
    n =set([int(i) for i in n])
    n =n.symmetric_difference(all_nums)
    n=sorted(n)
    return n
print(mobile_mis_num([9,8,6,4,1,2]))