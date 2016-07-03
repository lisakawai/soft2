import time

def quick_sort_impl(num, first, last):
	x = (num[first] + num[last]) / 2
	i = first
	j = last
	while True:
		while num[i] < x:
			i += 1
		while x < num[j]:
			j -= 1
		if i >= j:
			break
		tmp = num[i]; num[i] = num[j]; num[j] = tmp
		i += 1
		j -= 1
	if first < i - 1:
		quick_sort_impl(num, first, i-1)
	if j + 1 < last:
		quick_sort_impl(num, j + 1, last)

def quick_sort(num):
	quick_sort_impl(num, 0, len(num) - 1)


if __name__ == '__main__':
	f = open('quick.txt', 'w') 

	num = []
	for line in open('rand.txt', 'r'):
		itemList = line.split()
		for item in itemList:
			num.append( int(item) )
	
	for n in xrange(2,5001):
		num_calc = num[0:n]

		begin = time.time()
		quick_sort(num_calc)
		end = time.time()
		f.write('{} {}\n'.format(n, (end - begin)))

		#print num_calc

	f.close()