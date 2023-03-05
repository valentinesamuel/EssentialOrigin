class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def print_stack(self):
        current_node = self.top
        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next
        print(current_node.data)
        
    def peek(self):
        print(self.top.data)
        return self.top

    def push(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.top = newNode
            self.bottom = self.top
        else:
            newNode.next = self.top
            self.top = newNode
        self.length+=1

    def pop(self):
        if self.isEmpty():
            return
        dead_node = self.top
        self.top = self.top.next
        del dead_node
        self.length-=1

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def size(self):
        print(self.length)


stk = Stack()
stk.push("first")
stk.push("second")
stk.push("third")
# stk.peek()
# stk.pop()
stk.size()
stk.print_stack()