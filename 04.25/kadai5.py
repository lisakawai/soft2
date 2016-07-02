def fib(pre1, pre2, count, n):
	if count > n-1:
		print 'ans = %d\n' % pre1
	else:
		fib(pre2, pre1 + pre2, count+1, n) 


print 'please input number'
n = input()
pre1 = 1
pre2 = 1
fib(1, 1, 1,n)
