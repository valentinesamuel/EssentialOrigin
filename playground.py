class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return str(self.__dict__)
    
# from collections import deque

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
                        # Fetch the leftmost node of the right subtree of the current node
                        badNodeParent = badNode
                        badNode = badNode.left
                    currentNode.value = badNode.value
                    # Copy the values from the found node to the current node
                    if badNode == badNodeParent:
                        # if the badnode is the rightmost child of the currentnode,link the currentnode to the right node of the bad node
                        currentNode.right = badNode.right
                    if badNode.right == None:
                        # if the leftmost node of the right subtree of the currentnode has no right subtree. N/B that this left most node is a leaf node
                        badNodeParent.left = None
                        return
                    else:
                        # if the leftmost node of the right subtree of the currentnode has a  right subtree. N/B that this left most node has no left children but only a right subtree (child/children)
                        badNodeParent.left = badNode.right
                        return
                
                # No left or right children
                elif currentNode.left == None and currentNode.right == None:
                    if parentNode == None:
                        # if we didn't move from tne root Node  
                        self.root = None
                        return
                    # Since the currentnode is a leaf node with no child, both sides will be empty
                    if parentNode.value > currentNode.value:
                        parentNode.left = None
                        return
                    else:
                        parentNode.right = None
                        return

                # Only left child
                elif currentNode.left != None and currentNode.right == None:
                    # if we didn't move from tne root Node  
                    if parentNode == None:
                        self.root = None
                        return
                    if parentNode.value > currentNode.value:
                        # link the parent node to the node after the currentnode to keep everything in order
                        parentNode.left = currentNode.left
                        return
                    else:
                        # since the currentnode is bigger than the parent node, the left node after the current node will be bigger than the parent node so it has to be on the right of the parent node so that the right node after the current node will be correct in its position by remaining on the right of the new currentnode
                        parentNode.right = currentNode.left
                        return

                # Only right child
                elif currentNode.left == None and currentNode.right != None:
                    if parentNode == None:
                        self.root = None
                        return
                    if parentNode.value > currentNode.value:
                        parentNode.left = currentNode.right
                        return
                    else:
                        parentNode.right = currentNode.right
                        return
        return ("Not Found")        
        
    def breadthFirstSearch(self):
        current_node = self.root
        result = []
        queue = [] # queue = deque()
        queue.append(current_node) 

        while len(queue) > 0:
            current_node = queue.pop(0) # queue.popleft()
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return result
        
    def breadthFirstSearchRecursive(self, queue, result):
        if not len(queue):
            return result
        
        current_node = queue.pop(0) # queue.popleft()
        result.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        
        return self.breadthFirstSearchRecursive(queue, result)



def shift(arr):
    if len(arr) <= 1:
        return arr
    return arr[1:]

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(13)
bst.insert(65)
bst.insert(0)
bst.insert(10)
# print(bst)
# print(bst.breadthFirstSearch())
print(bst.breadthFirstSearchRecursive([bst.root],[]))

