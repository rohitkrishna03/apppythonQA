# 2 Implement the mul method for the Vector class of Section 2.3.3, so
# that the expression v 3 returns a new vector with coordinates that are 3
# times the respective coordinates of v.
# R-2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
# class of Section 2.3.3, to provide support for the syntax v 3. Implement
# the rmul method, to provide additional support for syntax 3 v.
# R-2.14 Implement the mul method for the Vector class of Section 2.3.3, so
# that the expression u v returns a scalar that represents the dot product of
# the vectors, that is, ∑d
# i=1 ui · vi.

class vector:
    def __init__(self, *args):
        """initialize the vector with the multiple values"""
        if len(args) ==1 and  isinstance(args[0], list):
            self.coordinates=args[0]
        else:
            self.coordinates =list(args)
            
            
        
    def __repr__(self):
        """return the representation of the vector"""
        return f"vector({self.coordinates})"
        
        
    def __mul__(self,other):
        """support the scale of multiplication of the vectors"""
        if isinstance(other, [(int, float)]):
            return vector([x * other for c in self.coordinates])
        elif isinstance(other, vector):
            return sum(self.coordinates[i] * other.coordinates[i] for i in range(len(self.coordinates)))
        else:
            return NotImplemented
        
    def __rmul__(self, other):
        """support the scalar multiplication * v"""
        return self._mul(other)
    def __neg__(self,other):
        return  ([-x for x in self.coordinates])
    
v = vector(1,2,3)

result1 =v * 3
result2 =3*v

u = vector(4,5,6)
dot_product = u*v
print(f"the dot product is ${dot_product}")
            
            
            