class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recoverFromPreorder(traversal):
    if not traversal:
        return None
    
    stack = []
    i = 0
    
    while i < len(traversal):
        depth = 0
        while i < len(traversal) and traversal[i] == '-':
            depth += 1
            i += 1
        
        value = 0
        while i < len(traversal) and traversal[i].isdigit():
            value = value * 10 + int(traversal[i])
            i += 1
        
        node = TreeNode(value)
        
        while len(stack) > depth:
            stack.pop()
        
        if stack:
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
        
        stack.append(node)
    
    return stack[0]

def printTree(root):
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    return result



# Приклад 1
traversal1 = "1-2--3--4-5--6--7"
result1 = recoverFromPreorder(traversal1)
print(printTree(result1))
# Виведе [1, 2, 5, 3, 4, 6, 7]

# Приклад 2
traversal2 = "1-2--3---4-5--6---7"
result2 = recoverFromPreorder(traversal2)
print(printTree(result2))

# Приклад 3
traversal3 = "1-401--349---90--88"
result3 = recoverFromPreorder(traversal3)
print(printTree(result3))
