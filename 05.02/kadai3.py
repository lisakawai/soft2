class Rat:
    numer = 0
    denom = 0
    
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        
    def __add__(self, other):
    	numer_new = self.numer * other.denom + self.denom * other.numer
    	denom_new = self.denom * other.denom
        return Rat(numer_new, denom_new)

    def __mul__(self, other):
    	numer_new = self.numer + other.numer
    	denom_new = self.denom + other.denom
    	return Rat(numer_new, denom_new)

    def __str__(self):
    	return "answer = %d/%d" % (self.numer, self.denom)

    def print_info(self):
        print ("%d/%d" % (self.numer, self.denom))
    

def linear_combination(a, b, c, d):
	if isinstance(a, Rat):
		print a * c + b * d
	else:
		print a * c + b * d
		

one_half = Rat(1,2)
one_third = Rat(1,3)
one_half.print_info()
one_third.print_info()
print one_third + one_half

linear_combination(1, 2, 3, 4)
linear_combination(one_half, one_half, one_third, one_third)
