class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
    
    def intersect(self,other):
        commonNum = intSet()
        for num in other.vals:
            if num in self.vals:
                commonNum.insert(num)
        return commonNum
                
    def __len__(self):
        return len(self.vals)

s1=intSet()
s2=intSet()
s1.vals = [1,2,3]
s2.vals = [2,4,6]
print(s1.intersect(s2))

#s = intSet()
#print(s)
#s.insert(3)
#s.insert(4)
#s.insert(3)
#print(s)
#s.member(3)
#s.member(5)
#s.insert(6)
#print(s)
#s.remove(3)
#print(s)
##s.remove(3)
