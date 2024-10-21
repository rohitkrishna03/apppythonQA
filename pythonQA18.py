# Write a Python program to test whether a passed letter is a vowel or not
str=input("enter anu word : ")
vowels = 'aeiou'
def is_vow(str,vowels):
    if str in vowels:
        return "it cintains vowels"
    else:
        return "no vowels found"
print(is_vow(str, vowels))
