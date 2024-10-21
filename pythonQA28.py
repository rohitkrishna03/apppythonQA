# Write a Python program to create a histogram from a given list of integers.

hist = input("enter the list you want to print: ")
hist_list =[int(x) for x in hist.split()]

def histogram(hist_list):
    for n in hist_list:
        output=''
        times=n
        
        while times>0:
            output+='*'
            times = times-1
            
        print(output)
        
histogram(hist_list)