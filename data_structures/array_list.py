class ArrayList():
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        if (index > self.length - 1):
            return
        return self.data[index]

    def push(self, item):
        self.length += 1
        self.data[self.length - 1] = item

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def insert(self, index, item):
        """
add a new slot by expanding the length of the array, starting from the empty slot, loop backward and the current item should be the previous item in the array. This creates space for the new item. So long as we are using range and stoping at index, this means the swapping of values will not be done on index position since range always stops at - 1
  		"""
        if (index > self.length):
            return "Index is greater than the last_item + 1"
        self.length += 1
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = item

    def delete(self, index):
        """
  	starting from the index of the item to be deleted to second last item(becasue of range), swap current value with the right neightbour's value. This moves the values to the left and delete the last index which is a duplicate of self.length - 1 becasue of range	
	"""
        if (index > self.length - 1):
            return
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1

    def reverse(self):
        low = 0
        high = self.length - 1
        while (low < high):
            self.data[low], self.data[high] = self.data[high], self.data[low]
            low += 1
            high -= 1

    def sortAscending():
        pass

    def sortDescending():
        pass


arr = ArrayList()
arr.push("first")
arr.push("second")
arr.push("third")
arr.push("fourth")
arr.push("fifth")
arr.push("sixth")
arr.push("seventh")
arr.reverse()
# arr.delete(0)
print(arr)
