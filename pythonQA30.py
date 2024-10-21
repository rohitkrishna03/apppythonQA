# Write a  Python program to calculate sum of digits of a number.

num = int(input("enter the number of 4 digits: "))

x = num//1000
x1 =(num-x*1000)//100
x2 =(num -x * 1000 -x1 *100)//10
x3 =num -x* 1000 -x1 * 100 - x2 *10
print("sum of all the x's :", x+x1+x2+x3)