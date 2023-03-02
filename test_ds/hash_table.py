class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __str__(self) -> str:
        return str(self.__dict__)
    
    def _hash(self, key):
        hash = 0
        for idx in range(len(key)):
            hash = (hash + ord(key[idx]) * idx) % self.size
        return hash
    
    def set(self, key, value):
        hash = self._hash(key)
        if self.data[hash]:
            self.data[hash].append([key, value])
        else:
            self.data[hash] = [[key, value]]
        return hash

    
    def get(self, item):
        key = self._hash(item)
        target = self.data[key]
        if target:
            for ele in target:
                if ele[0] == item:
                    print(ele[1])
        return None

    
hs = HashTable(5)
hs.set('grapes', 100000)
hs.set('oranges', 600)
hs.get('grapes')
print(hs)