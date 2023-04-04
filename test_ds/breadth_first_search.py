def breadthFirstSearchRecursive(queue, result):
    if not len(queue):
        return result

    current_node = queue.pop(0)
    result.append(current_node.value)

    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)

    return breadthFirstSearchRecursive(queue, result)

def breadFirstSearchIterative(rootNode):
    current_node = rootNode
    queue = []
    result = []

    queue.append(current_node)

    while queue > 0:
        current_node = queue.pop(0)
        result.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return result
            
# print(bst.breadthFirstSearchRecursive([bst.root],[]))