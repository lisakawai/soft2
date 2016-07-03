import random
import time

def hsearch(n, data):
	h = n % 100
	if not hash_table.has_key(h):
		return False
	else:
		for num in hash_table[h]:
			if num == n:
				return True
	return False

def make_hash(num):
	for n in num:
		h = n % 100
		if h not in hash_table:
			hash_table[h] = []
		hash_table[h].append(n)


   
    
num = []
for line in open('rand.txt', 'r'):
    itemList = line.split()
    for item in itemList:
        num.append( int(item) )
    
f = open('hash3-2.txt', 'w') 

for x in xrange(5001):
	hash_table = {}
	part_num = num[:x]

	
	make_hash(part_num)
	y = random.randint(1, 5000)
	begin = time.time()
	ans = hsearch(y, part_num)
	end = time.time()
	
	f.write('{} {}\n'.format(x, (end - begin)))

f.close()