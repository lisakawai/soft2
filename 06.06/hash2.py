import hashlib

def hsearch(n, data):

	h = hashlib.md5(n).hexdigest()
	if not hash_table.has_key(h):
		return False
	#return hsearch(n, hash_table[h])
	return True

hash_table = {}

def make_hash(num):
	for n in num:
		h = hashlib.md5(n).hexdigest()
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
    
