def insertionSort(arr):
    for i in range(1, len(arr)):
        min = i
        while min > 0 and arr[min] < arr[min-1]:
            arr[min], arr[min-1] = arr[min-1], arr[min]
            min-=1
    return arr

def selectionSort(arr):
    for idx1 in range(len(arr)):
        min = idx1
        for idx2 in range(idx1+1, len(arr)):
            if arr[min] > arr[idx2]:
                min = idx2
        arr[min], arr[idx1] = arr[idx1], arr[min]
    return arr

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quickSort(arr, left, right):
    if len(arr) <= 1:
        return arr

    if left < right:    
        partition_idx = partition(arr, left, right)
        left = quickSort(arr, left, partition_idx-1)
        right = quickSort(arr, partition_idx+1, right)

    return arr

def partition(arr, left, right):
    pivot = arr[right]
    part_at = left

    for j in range(left, right):
        if arr[j] < pivot:
            arr[j], arr[part_at] = arr[part_at], arr[j]
            part_at += 1
    
    arr[part_at], pivot = pivot, arr[part_at]
    return part_at

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result += left[i:]
    result += right[j:]

    return result

def bfs(queue, result):
    if not len(queue):
        return result

    cur_node = queue.pop(0)
    result.append(cur_node.value)

    if cur_node.left:
        queue.append(cur_node.left)
    if cur_node.right:
        queue.append(cur_node.right)

    return bfs(queue, result)

def inorder(node, result):
    if node.left:
        inorder(node.left, result)
    result.append(node.value)
    if node.right:
        inorder(node.right, result)
    return result

def postorder(node, result):
    if node.left:
        postorder(node.left, result)
    if node.right:
        postorder(node.right, result)
    result.append(node.value)
    return result

def preorder(node, result):
    result.append(node.value)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)
    return result

lst = [2, 4, 7, 2, 6, 8, 12, 1, 0]
print(insertionSort(lst))
print(selectionSort(lst))
print(bubbleSort(lst))
print(quickSort(lst, 0, len(lst)-1))
print(mergeSort(lst))
# bfs([self.root],[])
# dfsinorder(self.root,[])
# dfspostorder(self.root,[])
# dfspreorder(self.root,[])
