class Array:
    def __init__(self) -> None:
        self.length = 0
        self.data = {}
    def __str__(self) -> str:
        return str(self.__dict__)

    def append(self, item):
        self.length+=1
        self.data[self.length - 1] = item
    
    def clear(self):
        for idx in range(len(self.data)):
            del self.data[idx]
        self.length = 0
    
    def copy(self):
        newArray = {}
        newArray['length'] = self.length
        newArray['data'] = self.data
        return newArray
        
    def count(self):
        return self.length
    
    def extend(self, list):
        for idx in range(len(list)):
            self.append(list[idx])
    
    def index(self, item):
        for idx in range(self.length):
            if self.data[idx] == item:
                return(self.data[idx], idx)
            
    def insert(self, item, index):
        self.length+=1
        for idx in range(self.length - 1, index, -1):
            self.data[idx] = self.data[idx - 1]
        self.data[index] = item

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length-=1
        return last_item
    
    def delete_at_index(self, index):
        for idx in range(index, self.length - 1):
            self.data[idx] = self.data[idx + 1]
        del self.data[self.length - 1]
        self.length-=1

    def reverse(self):
        left_pointer = 0
        right_pointer = self.length- 1
        while left_pointer < right_pointer:
            self.data[left_pointer], self.data[right_pointer] = self.data[right_pointer], self.data[left_pointer]
            left_pointer+=1
            right_pointer-=1
               
    def sort(self):
        pass

arr = Array()
arr.append('girl')
arr.append('woman')
arr.extend(['man', 'boy', 'nigga', 'babe'])
print(arr)
