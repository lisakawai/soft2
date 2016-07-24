from numpy import * 
import scipy.linalg

a = array([[1.0, 1.0/2, 1.0/3], [1.0/2, 1.0/3, 1.0/4], [1.0/3, 1.0/4, 1.0/5]])
b = array([1.0, 2.0, 3.0])
print "a= ", a
print "b= ", b
x = linalg.solve(a, b)
print "x= ", x
print "check=", dot(a, x)
