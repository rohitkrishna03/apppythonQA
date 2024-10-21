# Write a Python program to display the current date and time.

import datetime
print("this is the current time")

now = datetime.datetime.now()

print(now.strftime("%Y-%m-%d %H:%M:%S"))
