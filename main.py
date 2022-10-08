class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        """Adds a new node to the end of a singly linked list

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
            self.tail = newNode
            self.length+=1
    
    def prepend(self, data):
        """Add a node to the head of a linked list

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
            self.head = newNode
            self.length +=1
        
    def print_list(self):
        """Prints all the values in a linked list
        """                
        currentNode = self.head
        while currentNode.next != None:
            print(currentNode.value, end= ', ')
            currentNode = currentNode.next    
        print(currentNode.value)
    
    def insert(self, data, index):
        """insert a node at any point in the linked list

        Args:
            data (any): the data to be added
            index (int): the position of the linked list

        Raises:
            IndexError: If the index is greater than the length of the linked list
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
            self.length+=1
    
    def remove_by_index(self, index):
        """Remove a node in the linked list by passing the index

        Args:
            index (int): the postion of the linked list

        Raises:
            IndexError: if the index does not exist
        """        
        if index > self.length:
            raise IndexError('Index out of range')
        elif index == 0:
            self.head = self.head.next
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
            del deadNode
            self.length-=1
        
    def remove_by_value(self, data):
        """Remove a node in the linked list by passing the value

        Args:
            data (any): the value of the node in the linked list

        Returns:
            Boolean: the availablity of the item in the linked list
        """        
        currentNode = self.head
        deadNode = currentNode.next
        while currentNode.next != None:
            if deadNode.value == data:
                currentNode.next = deadNode.next
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
           
                
        
linked_list = SinglyLinkedList()
linked_list.append(3)
linked_list.append(5)
linked_list.append("hi")
linked_list.prepend("holla")
linked_list.insert("testing", 2)
linked_list.append(13)
linked_list.append(46)
linked_list.remove_by_index(2)
linked_list.remove_by_value('hi')
linked_list.print_list()
linked_list.reverse()
linked_list.print_list()
