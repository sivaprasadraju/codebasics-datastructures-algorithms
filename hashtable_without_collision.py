class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(0, self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val): # add function
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key): # get function
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key): # delete function
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t['siva'] = 121231
t['mahesh'] = 121233
print(t.arr)
print(t['mahesh'])
