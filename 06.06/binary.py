import random

def bsearch(n, data):
	low = 0
	high = len(data) - 1
	while low <= high:
		middle = (low + high) / 2
		if n == data[middle]:
			return True
		elif n > data[middle]:
			low = middle + 1
		else:
			high = middle - 1
	return False


if __name__ == '__main__':
   # f = open('counting.txt', 'w') 

    num = []
    for line in open('rand.txt', 'r'):
        itemList = line.split()
        for item in itemList:
            num.append( int(item) )

n = random.randint(1,5000)
print bsearch(n, num)
