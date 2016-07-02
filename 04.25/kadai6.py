print 'please input number'
n = input()
a = 1
b = 1
for i in range(1,n-1):
	temp = a
	a = b
	b += temp
	i += 1	

print 'ans is %d\n' % b
