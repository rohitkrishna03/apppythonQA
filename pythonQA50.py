import collections

num = [1,2,3,4,5,6,7,8,9]
result = sum(collections.Counter(num).values())
print(result)
