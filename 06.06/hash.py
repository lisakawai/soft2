
def hsearch(n, data):
	h = n % 10
	if not hash_table.has_key(h):
		return False
	return hsearch(n, hash_table[h])

hash_table = {}

def make_hash(num):
	for n in num:
		h = n % 10
		if not hash_table.has_key(h):
			hash_table[h] = []
		hash_table[h].append(n)


if __name__ == '__main__':
   # f = open('counting.txt', 'w') 

    num = []
    for line in open('rand.txt', 'r'):
        itemList = line.split()
        for item in itemList:
            num.append( int(item) )

    
make_hash(num)
print hsearch(192, num)
print hsearch(193, num)
    
    