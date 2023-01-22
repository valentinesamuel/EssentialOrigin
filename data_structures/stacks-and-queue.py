class Node:
    def __init__(self, data) -> None:
        self.item = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            temp_node = self.top
            self.top = new_node
            self.top.next = temp_node
        self.length+=1
    
    def peek (self):
        if self.top is None:
            return None
        return self.top.item

    def pop(self):
        if self.length == 0:
            print('Empty Stack')
        else:
            temp_node = self.top
            self.top = self.top.next
            del temp_node
            self.length-=1
            if self.length == 0:
                self.bottom = None
        return
    
    def isEmpty(self):
        return self.top == None
    
    def print_stack(self):
        if self.top == None:
            print('Empty Stack')
        else:
            current_pointer = self.top
            while current_pointer is not None:
                print(current_pointer.item)
                current_pointer = current_pointer.next


myStack = Stack()
myStack.push('Hello')
myStack.push('Udemy')
myStack.push('Google')
print(myStack.isEmpty())
myStack.print_stack()