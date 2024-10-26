# we note that our Vector class supports a syntax such as
# v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
# a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
# Explain how the Vector class definition can be revised so that this syntax
# generates a new vector.
class vector:
    def __init__(self, *args):
        if len(args) ==1 and isinstance(args[0], list):
            self.coordinate =args[0]
        else:
            self.coordinate =list(args)
            
    def __repr__(self):
        return f"vector({self.coordinate})"
    
    
    def __add__(self, other):
        """add a vector to another vector or a list. """
        if isinstance(other, list):
            return vector([self.coordinate[i] +other[i] for i in range(len(self.coordinate))])
        elif isinstance(other, vector):
            return vector([self.coordinate[i] +other.coordinate[i] for i in range(len(other))])
        else:
            return NotImplemented
        
    def __radd__(self, other):
        """handle addition when the vector is on the right side of the operation"""
        if isinstance(other, list):
            return vector ([self.coordinate[i] + other[i] for i in range(len(other))])
        else:
            return NotImplemented
        
    def neg(self):
        """return a new vector with negated coordinates."""
        return vector([-x for x in self.coordinates])
    
u = vector(1,2,3)
result1 = u + [5, 3, 10]

print(f" u + [5, 3, 10] = {result1}")

result2 =[5, 3, 10] + u
print(f"[5, 3, 10] + u = {result2}")
    
    
    