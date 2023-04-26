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
        
sll = SinglyLinkedList()
sll.append(12)
sll.append(1)
sll.append(21)
sll.prepend('first')
sll.insert_at_index(2, 'checker')
sll.remove_at_index(3)
sll.print_list()
sll.reverse()
sll.print_list()
