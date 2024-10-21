text=input("enter any name/word: ")
n= int(input("enter no. of copies you need: "))
def string(text,n):
    result= ""
    for i in range(n):
        result =result + text
        
    return result
print(string(text,n))