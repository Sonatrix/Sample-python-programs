class Polynomial:
    def __init__(self,*coeffs):
        self.coeffs = coeffs
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)
    def __add__(self,other):
        return Polynomial(*(x+y for x,y in zip(self.coeffs,other.coeffs)))
    def __len__(self):
        return len(self.coeffs)
a = Polynomial(1,2,3)
b = Polynomial(3,4,5)

print(a)
print(b)
print(a+b)
