# Write a  Python program to find the heights of the top three buildings in descending order from eight given buildings.
print("input the heights of eight buildings: ")
l=[int(input()) for i in range(8)]
print("the heights of three building")
l = sorted(l)
print(*l[:4:-1], sep='\n')
