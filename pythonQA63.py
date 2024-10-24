# Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.
import random
def randint(a,b):
    
    return int(random.uniform(a,b+1))


def fun_shuffle(data):
    n =len(data)
    for i in range(n):
        j = randint(i, n-1)
        data[i],data[j]=data[j],data[i]
    
my_list =[1,2,3,4,5,6,7]
print("original list", my_list)
    
fun_shuffle(my_list)
print("shuffle my list", my_list)


# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.

def prod(a,b):
    if len(a) != len(b):
        raise ValueError("array must be od same length")
    n = len(a)
    c =[0]*n
    for i in range(n):
        c[i] =a[i]*b[i]
        
    return c
a =[1,2,3,4,5]
b =[2,3,4,5,6]
result =prod(a,b)

print("dot product of array c" ,result)

# Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

def add_to_list(my_list, index, values):
    try:
        my_list[index] = value
    except:
        print("dont try buffer overflow attack in python ")
        
my_list =[1,2,3,4,5,6]
index_to_write =10
value_to_write =99

add_to_list(my_list, index_to_write,value_to_write)

# Write a short Python function that counts the number of vowels in a given
# character string.

def count_vowels(input_string):
    vowels ='aeiosAEIOU'
    
    count =sum(1 for char in input_string if char in vowels)
    return count
string_to_check ='hwllo this is rohit'
vowel_count =count_vowels(string_to_check)
print(f"the number of vowels in '{string_to_check }' is : {vowel_count}")
    
# Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".

def rm_punch(s):
     punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     translator = str.maketrans('','',punctuation)
     return s.translate(translator)
sentence= "hello, that's the point i have tried to explain!"
cleaned_sentence= rm_punch(sentence)
print(f"without punctuation: {cleaned_sentence}")
    


    
    
    