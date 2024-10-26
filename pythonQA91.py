# Implement the sub method for the Vector class of Section 2.3.3, so
# that the expression u−v returns a new vector instance representing the
# difference between two vectors.
# R-2.10 Implement the neg method for the Vector class of Section 2.3.3, so
# that the expression −v returns a new vector instance whose coordinates
# are all the negated values of the respective coordinates of v.

class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __repr__(self):
        return f"vector({self.x}, {self.y})"
    def sub(self, other):
        """ return a new vector that is different from another vector"""
        return vector(self.x- other.x,self.y -other.y)
    def neg(self):
        return vector(-self.x, -self.y)
    
u = vector(3,4)
v = vector(1,2)

difference =u.sub(v)
print(f"u -v ={difference}")

negated_v =v.neg()
print(f"-v ={negated_v}")
