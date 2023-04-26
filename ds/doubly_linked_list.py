class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
     

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.length+=1

    def print_list(self):
        currentNode = self.head
        if currentNode == None:
            print("List is empty")
            return
        print('👇👇👇👇👇', end='\n')
        while currentNode.next != None:
            print(currentNode.data, end= ', ')
            currentNode = currentNode.next
        print(currentNode.data)
        print('👉👉',self.length)
        
    def prepend(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
    
    def insert_at_index(self, index, data):
        currentNode = self.head
        if index > self.length - 1:
            raise IndexError('Index out of range.')
        if currentNode == None:
            print('List is empty')
            return
        newNode = Node(data)
        position = 0
        while position < index - 1:
            currentNode = currentNode.next
            position+=1
        newNode.next = currentNode.next
        newNode.prev = currentNode
        currentNode.next = newNode
        self.length += 1
    
    def remove_at_index(self, index):
        currentNode = self.head
        if index > self.length - 1:
            raise IndexError('Index out of range.')
        if currentNode == None:
            print('List is empty')
            return
        position = 0
        while position < index - 1:
            currentNode = currentNode.next
            position+=1
        deadNode = currentNode.next
        currentNode.next = currentNode.next.next # or deadNode.next
        currentNode.next.prev = currentNode # or deadNode.next
        del deadNode
        self.length -= 1

    def lookup(self, data):
        findingNode = Node(data)
        currentNode = self.head
        if currentNode == None:
            print("List is empty")
            return
        while currentNode.next != None:
            if currentNode.data == findingNode.data:
                print('😁',currentNode.data)
            currentNode = currentNode.next

    def reverse(self):
        previous = None
        current = self.head
        following = self.head
        while current != None:
            following = following.next
            current.next = previous
            previous = current
            current = following
        self.head = previous
        
dll = DoublyLinkedList()
dll.append(12)
dll.append(1)
dll.append(21)
dll.prepend('first')
dll.insert_at_index(2, 'checker')
dll.remove_at_index(3)
dll.print_list()
dll.reverse()
dll.print_list()
