# Write a  Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
# Return the string unchanged if the given string already begins with "Is".
str =input("enter any word to check that starts wit is or not : " )
def check_string(str):
    if len(str) >=2 and str[:2] == "is":
        return str
    else:
        print("dont start with 'is'")
print(check_string(str))