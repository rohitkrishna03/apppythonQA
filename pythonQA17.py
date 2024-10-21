# Write a  Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
def string(text,n):
    flen=2
    if flen<len(text):
        flen=len(text)
    substr = text[:flen]
    result =""
    for i in range(n):
        result=result+substr
        return result
    
print(string('rohit',2))