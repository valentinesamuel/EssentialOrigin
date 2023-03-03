class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
     

class SinglyLinkedList:
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
        currentNode.next = newNode


sll = SinglyLinkedList()
sll.append(12)
sll.append(1)
sll.append(21)
sll.prepend('first')
sll.insert_at_index(2, 'checker')
sll.print_list()
