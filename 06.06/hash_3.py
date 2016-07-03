class HashTable3:
    def __init__(self, func, size):
        self.size = 0
        self.hash_size = size
        self.hash_func = func
        self.hash_table = [None] * size

    def _hash_func(self, key):
        n = self.hash_func(key)
        return (n % self.hash_size, 7 - n % 7)

    def _search_key(self, key):
        n, i = self._hash_func(key)
        count = 0
        while count < self.hash_size:
            data = self.hash_table[n]
            if data is None:
                break
            if data and data[0] == key:
                return n
            # double hashing
            n = (n + i) % self.hash_size
            count += 1
        return -1

    def search(self, key):
        n = self._search_key(key)
        if n >= 0: return True
        return False

    def insert(self, key, value):
        n = self._search_key(key)
        if n < 0:
            n, i = self._hash_func(key)
            count = 0
            while count < self.hash_size:
                if not self.hash_table[n]:
                    self.size += 1
                    break
                # double hashing
                n = (n + i) % self.hash_size
                count += 1
            else:
                raise IndexError
        # insert
        self.hash_table[n] = (key, value)
        return value

    def __len__(self): return self.size


if __name__ == '__main__':
    import random
    hs = 30
    def hf(key):
        value = 0
        for x in key:
            value = (value << 3) + x
        return value

    ht = HashTable3(hf, hs)
    count = 1
    keys = [(random.randint(0, 255),random.randint(0, 255)) for x in xrange(11)]
    for x in keys:
        if not ht.search(x):
            ht.insert(x, count)
            count += 1
   
    for x in keys:
        ht.insert(x, count)
        count += 1
    
       
    print ht.search(x)
