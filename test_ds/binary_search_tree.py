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
        if self.root == None: #Tree is empty
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while current_node!=None: #Traversing the tree to reach the desired node or the end of the tree
            if current_node.value > value:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.value < value:
                parent_node = current_node
                current_node = current_node.right
            else: #Match is found. Different cases to be checked
                #Node has left child only
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.value > current_node.value:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                #Node has right child only
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.value > current_node.value:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                #Node has neither left nor right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None: #Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.value > current_node.value:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                #Node has both left and right child
                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None: #Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.value = del_node.value #The value to be replaced is copied
                    if del_node == del_node_parent: #If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right == None: #If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else: #If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
        return "Not Found"

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


print(bst)