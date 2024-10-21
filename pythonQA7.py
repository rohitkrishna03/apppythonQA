# Write a  Python program that accepts a filename from the user and prints the extension of the file.

filename = input("enter the file name with entension: ")

str_name = filename.split(".")

print(f"the filename is {filename} and its extension is " + repr(str_name[-1]))