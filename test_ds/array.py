class Array:
    def __init__(self):
        self.data = {}
        self.length = 0
    
    def __str__(self) -> str:
        return f"Array(data = {self.data}, length = {self.length})"
    
    def append(self, item):
        self.length+=1
        self.data[self.length - 1] = item
    
    def clear(self):
        self.data = {}
        self.length = 0

    def copy(self):
        newArray = {}
        newArray['data'] = self.data
        newArray['length'] = self.length
    
    def count(self):
        return self.length

    def extend(self, arr):
        for item in arr:
            self.append(item)
    
    def index(self, item):
        for idx in self.data:
            if self.data[idx] == item:
                return self.data[idx]
    
    def insert(self, item, index):
        self.length += 1
        for idx in range(self.length - 1, index, -1):
            self.data[idx] = self.data[idx-1]
        self.data[index] = item

    def pop(self):
        del self.data[self.length - 1]
        self.length -=1
    
    def delete_at_index(self, index):
        self.length -= 1
        for idx in range(self.length, index):
            print(idx, idx-1)
            self.data[idx] = self.data[idx - 1]
        del self.data[index]

    def reverse(self):
        start = 0
        end = self.length-1
        while start < end:
            self.data[start], self.data[end] = self.data[end], self.data[start]
            start +=1
            end -=1


arr = Array()
arr.append('girl')
arr.append('woman')
arr.extend(['man', 'boy', 'nigga', 'babe'])
print(arr)
arr.reverse()
print(arr)
