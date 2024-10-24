# Write a  Python program to get the third side of a right-angled triangle from two given sides.

# Note: Use bitwise operations to add two numbers

def python_theorem(adj_side,opp_side,hypo_side):
    
    if opp_side == str('x'):
        return ("opposite = " + str(((hypo_side**2) - (adj_side**2))**0.5 ))
    
    elif adj_side == str('x'):
        return ("opposite = " + str(((hypo_side**2) - (opp_side**2))**0.5 ))
    
    if hypo_side == str('x'):
        return ("opposite = " + str(((opp_side**2) + (adj_side**2))**0.5 ))
    else:
        return "you got it!"
    
print(python_theorem(3, 4, 'x'))
print(python_theorem(3, 'x', 5))
print(python_theorem('x', 4, 5))
print(python_theorem(3, 4, 5))