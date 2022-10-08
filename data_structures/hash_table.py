class HashTable():
	def __init__(self, size):
		self.size = size
		self.data = [None]*self.size

	def __str__(self):
		return str(self.__dict__)

	def _hash(self,key):
		hash = 0
		for i in range(len(key)):
			hash = (hash + ord(key[i]) * i) % self.size
		return hash

	def set(self, key, value):
		hash = self._hash(key)
		if self.data[hash]:
			self.data[hash].append([key, value])
		else:
			self.data[hash] = [[key, value]]
		return hash

	def get(self, key):
		hash = self._hash(key)
		if self.data[hash]:
			for ele in self.data[hash]:
				if ele[0] == key:
					return ele[1]
		return None

	def keys(self):
		keysArray = []
		for ele in self.data:
			if ele:
				if len(ele) > 1:
					for inner_ele in ele:
						keysArray.append(inner_ele[0])
				else:
					keysArray.append(ele[0][0])
		print(keysArray)

	def values(self):
		valuesArray = []
		for ele in self.data:
			if ele:
				if len(ele) > 1:
					for innerele in ele:
						valuesArray.append(innerele[1])
				else:
					valuesArray.append(ele[0][1])
		print(valuesArray)

ht = HashTable(12)
ht.set('grapes', 1000)
ht.set('bananas', 401)
ht.set('alpine', 1)
ht.set('oranges', 12)
ht.set('oranges', 15)
ht.keys()
ht.values()
print(ht)
