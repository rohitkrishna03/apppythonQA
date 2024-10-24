# Write a  Python program to check the priority of the four operators (+, -, *, /).


from collections import deque
import re
__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}
def test_high_priority(operator1, operator2):
    return __priority__[operator1] >= __priority__[operator2]
print(test_high_priority('*','/'))