class Node:
    def __init__(self,value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        """Adds a new node to the end of a doubly linked list

        Args:
            data(any): the data to be added in the node
        """        
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.length+=1
    
    def prepend(self, data):
        """Add a node to the head of a doubly linked list

        Args:
            data (any): the data to be added
        """        
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head 
            self.length +=1
        else:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
            self.length +=1
        
    def print_list(self):
        """Prints all the values in a doubly linked list
        """                
        currentNode = self.head
        while currentNode.next != None:
            print(currentNode.value, end= ', ')
            currentNode = currentNode.next    
        print(currentNode.value)
    
    def print_list_reverse(self):
        """print the values of the doubly linked list in reverse order
        """        
        currentNode = self.tail
        while currentNode.previous != None:
            print(currentNode.value, end=", ")
            currentNode = currentNode.previous
        print(currentNode.value)
            
    def insert(self, data, index):
        """insert a node at any point in the doubly linked list

        Args:
            data (any): the data to be added
            index (int): the position of the doubly linked list

        Raises:
            IndexError: If the index is greater than the length of the doubly linked list
        """        
        newNode = Node(data)
        if index > self.length:
            raise IndexError("Index out of range")
        elif index == 0:
            self.prepend(newNode)
        else:
            currentNode = self.head
            index-=1
            while index > 0:
                currentNode = currentNode.next
                index-=1
            newNode.next = currentNode.next
            currentNode.next = newNode
            newNode.previous = currentNode
            newNode.next.previous = newNode
            self.length+=1
    
    def remove_by_index(self, index):
        """Remove a node in the doubly linked list by passing the index

        Args:
            index (int): the postion of the doubly linked list

        Raises:
            IndexError: if the index does not exist
        """        
        if index > self.length:
            raise IndexError('Index out of range')
        elif index == 0:
            self.head = self.head.next
            self.length-=1
        elif index == self.length-1:
            tempNode = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            del tempNode
            self.length-=1
        else:
            currentNode = self.head
            deadNode = currentNode.next
            index-=1
            while index > 0:
                currentNode = currentNode.next
                deadNode = currentNode.next
                index-=1
            currentNode.next = deadNode.next
            deadNode.next.previous = currentNode
            self.length-=1
        
    def remove_by_value(self, data):
        """Remove a node in the doubly linked list by passing the value

        Args:
            data (any): the value of the node in the doubly linked list

        Returns:
            Boolean: the availablity of the item in the doubly linked list
        """        
        currentNode = self.head
        deadNode = currentNode.next
        while currentNode.next != None:
            if deadNode.value == data:
                if deadNode == self.tail:
                    self.remove_by_index(self.length-1)
                    return
                currentNode.next = deadNode.next
                deadNode.next.previous = currentNode
                self.length-=1
                del deadNode
                return
            else:
                currentNode = currentNode.next
                deadNode = currentNode.next
        return "Data not found"
    
    def lookup(self, data):
        """Checks if an item exists in the linked list

        Args:
            data (any): the item to look for in the linked list
        """        
        currentNode = self.head
        while currentNode.next != None:
            if currentNode.value == data:
                print("Found😍")
                return
            else:
                currentNode = currentNode.next
            
                
        
# dll = DoublyLinkedList()
# dll.append(3)
# dll.append(5)
# dll.append("hi")
# dll.prepend("holla")
# dll.insert("testing",1)
# dll.append(13)
# dll.append(46)
# dll.remove_by_index(5)
# dll.remove_by_value(46)
# dll.lookup("holla")
# print(dll.length)
# dll.print_list()