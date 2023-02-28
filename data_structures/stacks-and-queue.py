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


# myStack = Stack()
# myStack.push('Hello')
# myStack.push('Udemy')
# myStack.push('Google')
# print(myStack.isEmpty())
# myStack.print_stack()

# Queues
class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            print('Empty Queue')
        else:
            return self.last.item
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.length != 0:
            self.last.next = new_node
            self.last = new_node
        else:
            self.first = new_node
            self.last = new_node
        self.length += 1
        return
    
    def dequeue(self):
        if self.length != 0:
            self.first = self.first.next
            self.length -=1
        else:
            print('Empty Stack')
        return
    
    def isEmpty(self):
        return self.last == None
    
    def print_queue(self):
        current_node = self.first
        while current_node != None:
            print(current_node.item)
            current_node = current_node.next
        print(f'Length is {self.length}')

my_queue = Queue()
my_queue.enqueue('Boy')
my_queue.enqueue('Man')
my_queue.enqueue('Girl')
print(my_queue.peek(), '....')
my_queue.dequeue()
my_queue.print_queue()