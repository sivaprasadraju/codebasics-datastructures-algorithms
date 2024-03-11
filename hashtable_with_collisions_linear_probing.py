class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(0, self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h]:
            updated_h = self.find_slot(key, h)
            self.arr[updated_h] = (key, value)
        else:
            self.arr[h] = (key, value)
        return

    def get_prob_range(self, index):
        return [*range(index, self.MAX)] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap is full")

    def __getitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index][0] == key:
                return self.arr[prob_index][1]
            if self.arr[prob_index][0] is None:
                return

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if prob_range[prob_index] is None:
                return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index][0] = None

if __name__ == '__main__':
    linear_probing_hashtable = HashTable()
    linear_probing_hashtable['march 6'] = 93
    linear_probing_hashtable['march 17'] = 34
    print(linear_probing_hashtable['march 6'])
    print(linear_probing_hashtable['march 17'])

