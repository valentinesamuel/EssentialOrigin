class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def __repr__(self):
        return str(self.__dict__)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __repr__(self):
        return str(self.__dict__)

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if currentNode.value > newNode.value:
                    if currentNode.left == None:
                        currentNode.left = newNode
                        return
                    currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        currentNode.right = newNode
                        return
                    currentNode = currentNode.right


    def lookup(self, value):
        newNode = Node(value)
        if self.root == None:
            print('Empty Tree')
            return
        else:
            currentNode = self.root
            while True:
                if currentNode.value > newNode.value:
                    if currentNode.value == newNode.value or currentNode.left.value == newNode.value or currentNode.right.value == newNode:
                        print("Found")
                        return
                    if currentNode.left == None:
                        return
                    currentNode = currentNode.left
                else:
                    if currentNode.value == newNode.value or currentNode.left.value == newNode.value or currentNode.right.value == newNode:
                        print("Found")
                        return 
                    if currentNode.right == None:
                        return
                    currentNode = currentNode.right
        
    def lookup2(self, value):
        newNode = Node(value)
        if self.root == None:
            print('Empty Tree')
            return
        currentNode = self.root
        while currentNode:
            if value > currentNode.value:
                currentNode = currentNode.left
            elif value < currentNode.value:
                currentNode = currentNode.right
            elif currentNode.value == newNode.value:
                print("Found")
                return currentNode
        print("Not Found")
        return None

    def remove(self, value):
        pass

def traverse(node):
    tree = {'value': node.value}
    tree.left = None if node.left == None else traverse(node.left)
    tree.right = None if node.right == None else traverse(node.right)
    return tree

bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(150)
bst.insert(15)
bst.insert(100)
bst.insert(22)
bst.insert(-1)
bst.lookup2(0)
# print(bst)

