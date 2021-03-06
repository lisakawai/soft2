import time

def merge(num, left, right, size):
	tmp = [0]*(left + size)
	i = left; j = right
	k = left; l = left + size
	while i < right and j < l:
		if num[i] < num[j]:
			tmp[k] = num[i]; i += 1
		else:
			tmp[k] = num[j]; j += 1
		k += 1
	if i < right:
		for h in range(i, right):
			tmp[k] = num[h]; k += 1
	if j < l:
		for h in range(j, l):
			tmp[k] = num[h]; k += 1
	for h in range(left, l):
		num[h] = tmp[h]

def merge_sort_impl(num, left, right):
	if left < right:
		middle = int((right + left) / 2)
		merge_sort_impl(num, left, middle)
		merge_sort_impl(num, middle + 1, right)
		merge(num, left, middle + 1, right - left + 1)

def merge_sort(num):
	merge_sort_impl(num, 0, len(num) - 1)


if __name__ == '__main__':
	f = open('merge.txt', 'w') 

	num = []
	for line in open('rand.txt', 'r'):
		itemList = line.split()
		for item in itemList:
			num.append( int(item) )
	
	for n in xrange(2,5001):
		num_calc = num[0:n]

		begin = time.time()
		merge_sort(num_calc)
		end = time.time()
		f.write('{} {}\n'.format(n, (end - begin)))

		#print num_calc

	f.close()

