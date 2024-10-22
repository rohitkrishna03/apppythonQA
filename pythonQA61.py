# # # # age =-1
# # # # while age<=0:
# # # #     try:
# # # #         age =int(input("enter the age in years : "))
# # # #         if age <= 0:
# # # #             print("your age must be in positive values")
# # # #     except(ValueError, EOFError):
# # # #         print('invalid opeator')
        
        
  
  
# # # # list comprehension in python

# # # num =[1,2,3,4,5] 
# # # odd_num =[n for n in num if n % 2 !=0]
# # # print(odd_num)

# # # # another example fo the list comprehension

# # # str =["hoodie","goodie","puddie","meddies","cat","rat"]
# # # short_word =[alph for alph in str if len(alph) <=5]
# # # print(short_word)

# # # # set comprehension in python
# # # numbers = [1,2,3,4,5,6,7]
# # # squared_num ={x**2 for x in numbers}
# # # print(squared_num)

# # # # simultaneous assignment for packing and unpacking in python
# # # a,b =4,8
# # # print("value  assigned to a is : ", a)
# # # print("value  assigned to b is  : ", b)

# # # # * is used foe deep unpacking
# # # fruits = ["apple", "banana", "cherry", "orange" ,"kiwi","mango"]
# # # x ,*last = fruits
# # # print(*last)

# # # # next = (a*current + b) % n;
# # # # where a, b, and n are appropriately chosen integers. Python uses a more advanced
# # # # technique known as a Mersenne twister. It turns out that the sequences generated
# # # # by these techniques can be proven to be statistically uniform, which is usually
# # # # good enough for most applications requiring random numbers, such as games.

# # # squared_sqr ={2**i for i in range(9)}
# # # print(squared_sqr)

# # # # Demonstrate how to use Python’s list comprehension syntax to produce
# # # # the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

# # # # What parameters should be sent to the range constructor, to produce a
# # # # range with values 50, 60, 70, 80?
# # # range_prd ={10*i for i in range(5,9)}
# # # print(range_prd)


# # # # What parameters should be sent to the range constructor, to produce a
# # # # range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

# # # point_range={1*i for i in range(8,-10,-2)}
# # # print(point_range)
# # # print(list(point_range))

# # # # Write a short Python function that takes a positive integer n and returns
# # # # the sum of the squares of all the positive integers smaller than n.
# # # def sum_square(n):
# # #     return sum(i**2 for i in range(1,n))

# # # n= int(input("enter the value of n: "))
# # # result = sum_square(n)
# # # print(f"the square of the give n is: {result}")

# # # 2 Python’s random module includes a function choice(data) that returns a
# # # random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
# # # the built-in range function, that return a random choice from the given
# # # range. Using only the randrange function, implement your own version
# # # of the choice function.

# # import random
# # def my_choice(data):
# #     if len(data) ==0:
# #         print("the given data is empty")
# #     random_index = random.randrange(len(data))
# #     return data[random_index]
        
# # data =[10,20,30,40,50]
# # random_element =my_choice(data)
# # print(f"random_element :{random_element}")

# # Write a pseudo-code description of a function that reverses a list of n
# # integers, so that the numbers are listed in the opposite order than they
# # were before, and compare this method to an equivalent Python function
# # for doing the same thing.
# def reverse_list(lst):
#     left =0
#     right = len(lst)-1
    
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
        
#         left +=1
#         right -=1
        
#     return lst
# lst =[1,2,3,4,5]
# reversed_list =reverse_list(lst)
# print(reversed_list)

lst =[1,2,3,4,5]
reversed_list =lst[::-1]
print(reversed_list)
lst.reverse()
print(lst)


