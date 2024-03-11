class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(0, self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val): # add function
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, val)
                found = True
                break
        if not found:
                self.arr[h].append((key, val))

    def __getitem__(self, key): # get function
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    def __delitem__(self, key): # delete function
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashTable()
t['march 6'] = 34
t['march 6'] = 45
t['march 17'] = 412

del t['march 17']
del t['march 6']
print(t['march 17'])
print(t['march 6'])

