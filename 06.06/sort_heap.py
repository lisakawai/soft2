#-*- coding: utf-8 -*-
import time

def heap_add(num, c):
	while True:
		p = (c-1) / 2 #親のindexを計算
		if p < 0 :
			break
		#親の方が小さい場合はbreak
		if num[p] <= num[c]:
			break
		#num[p], num[c] = num[c], num[p]
		tmp = num[p]; num[p] = num[c]; num[c] = tmp
		c = p #親ノードを新たな子ノードにする

def heap_del(num, length, p):
	while True:
		c = p * 2 + 1 #子のindexを計算
		if c >= length:
			break
		if c + 1 < length and num[c + 1] <= num[c]:
			c = c + 1
		# 親の方が小さい場合はbreak
		if num[p] <= num[c]:
			break
		tmp = num[p]; num[p] = num[c]; num[c] = tmp
		p = c #子ノードを新たな親ノードにする

def heap_sort(num):
	for i in range(1, len(num)):
		#最初のヒープを作る
		heap_add(num, i)
	for i in range(len(num)):
		tmp = num[len(num) - 1 - i] #num[-1]
		num[len(num) - 1 - i] = num[0]
		num[0] = tmp
		heap_del(num, len(num) - 1 - i, 0)
	# 逆順にする
	for i in range(len(num) / 2):
		tmp = num[i]
		num[i] = num[len(num) - i - 1]
		num[len(num) - i - 1] = tmp


if __name__ == '__main__':
	f = open('heap.txt', 'w') 

	num = []
	for line in open('rand.txt', 'r'):
		itemList = line.split()
		for item in itemList:
			num.append( int(item) )
	
	for n in xrange(2,5001):
		num_calc = num[0:n]

		begin = time.time()
		heap_sort(num_calc)
		end = time.time()
		f.write('{} {}\n'.format(n, (end - begin)))

		#print num_calc

	f.close()

