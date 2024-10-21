str =input("enter any value to know if it is numeric : ")
try:
    i = float(str)
except(ValueError, TypeError):
    print("not a numeric")
    
print()
