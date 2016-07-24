#-*- coding: utf-8 -*-
import math

a = [[0 for i in range(2)] for j in range(2)]
a[0][0] = 1
a[0][1] = 2
a[1][0] = 3
a[1][1] = 4


# A = [[1,2],[3,4]]

#　特性方程式
#  (a[0][0] - x) * (a[1][1] - x) - a[1][0] * a[0][1] = 0
#  p * x * x + q * x + r = 0

p = 1.0
q = - a[1][1] - a[0][0]
r = a[1][1] * a[0][0] - a[1][0] * a[0][1]

ans1 = (-q + math.sqrt(q * q - 4 * p * r))/ (2 * p)
ans2 = r / (p * ans1)
print "１つ目の固有値は", ans1
print "２つ目の固有値は", ans2