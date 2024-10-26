# Write a  Python program to compute the digit number of the sum of two given integers.
print("input integers(a,b) : ")
a,b =map(int, input().split(" "))
print("number of digits a and b : ")
print(len(str(a+b)))
