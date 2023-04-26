class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        print(self.first.data)
        return self.first

    def print_queue(self):
        current_node = self.first
        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next
        print(current_node.data)


    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node 
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return
        else:
            dead_node = self.first
            self.first = self.first.next
            del dead_node
        self.length -= 1

    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False

que = Queue()
que.enqueue("first")
que.enqueue("second")
que.enqueue("third")
que.enqueue("fourth")
que.dequeue()
que.peek()
que.print_queue()