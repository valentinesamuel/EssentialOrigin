class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return str(self.__dict__)

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def __repr__(self) -> None:
        return str(self.__dict__)

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return
        currentNode = self.root
        while True:
            if currentNode.value > newNode.value:
                if currentNode.left == None:
                    currentNode.left = newNode
                    return
                currentNode = currentNode.left
            if currentNode.value < newNode.value:
                if currentNode.right == None:
                    currentNode.right = newNode
                    return
                currentNode = currentNode.right        

    def lookup(self, value):
        if self.root == None:
            print("Empty Tree")
            return
        currentNode = self.root
        while currentNode:
            if currentNode.value > value:
                currentNode = currentNode.left
            elif currentNode.value < value:
                currentNode = currentNode.right
            elif currentNode.value == value:
                print("Found")
                return currentNode
        print("Not Found")
        return None
    
    def remove(self, value):
        if self.root == None:
            return "Empty List"
        currentNode = self.root
        parentNode = None
        while currentNode != None:
            if currentNode.value > value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif currentNode.value < value:
                parentNode = currentNode
                currentNode = currentNode.right
            else: # A match has been found
                # Both left and right children
                if currentNode.left != None and currentNode.right != None:
                    badNode = currentNode.right
                    badNodeParent = currentNode.right
                    while badNode.left != None:
                        badNodeParent = badNode
                        badNode = badNode.left
                    currentNode.value = badNode.value
                    if badNode == badNodeParent:
                        currentNode.right = badNode.right
                    if badNode.right == None:
                        badNodeParent.left = None
                        return
                    else:
                        badNodeParent.left = badNode.right
                        return
                
                # No left or right children
                elif currentNode.left == None and currentNode.right == None:
                    if parentNode == None:
                        self.root = None
                        return
                    if parentNode.value > currentNode.value:
                        parentNode.left = None
                        return
                    else:
                        parentNode.right = None
                        return

                # Only left child
                elif currentNode.left != None and currentNode.right == None:
                    if parentNode == None:
                        self.root = None
                        return
                    if parentNode.value > currentNode.value:
                        parentNode.left = currentNode.left
                        return
                    else:
                        parentNode.right = currentNode.left
                        return

                # Only right child
                elif currentNode.left == None and currentNode.right != None:
                    if parentNode == None:
                        self.root = None
                    if parentNode.value > currentNode.value:
                        parentNode.left = currentNode.right
                        return
                    else:
                        parentNode.right = currentNode.right
                        return
        return ("Not Found")        
        

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(13)
bst.insert(65)
bst.insert(0)
bst.insert(10)
'''
            5
        3       7
    1               13
0                10     65
'''

(bst.remove(13))
'''
            5
        3       7
    1               65
0                10     
'''
bst.remove(5)
'''
            7
        3       65
    1        10     
0                
'''
bst.remove(3)
'''
            7
        1       65
    0        10                     
'''
bst.remove(7)
'''
            10
        1       65
    0                
'''
bst.remove(1)
'''
            10
        0       65
'''

print(bst)
