def depthFirstSearch(node, result):
    in_order(node, result)
    pre_order(node, result)
    post_order(node, result)

def in_order(node, result):
    if node.left:
        in_order(node.left, result)
    result.append(node.value)
    if node.right:
        in_order(node.right, result)
    return result

def pre_order(node, result):
    result.append(node.value)
    if node.left:
        pre_order(node.left, result)
    if node.right:
        pre_order(node.right, result)
    return result

def post_order(node, result):
    if node.left:
        post_order(node.left, result)
    if node.right:
        post_order(node.right, result)
    result.append(node.value)
    return result

# print(depthFirstSearch(self.root, []))