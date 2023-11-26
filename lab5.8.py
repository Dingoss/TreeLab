from collections import defaultdict
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order_traversal(root):
    if not root:
        return []

    queue = deque([(root, 0, 0)]) 
    positions = defaultdict(list)

    while queue:
        node, row, col = queue.popleft()
        positions[col].append((row, node.val))

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    result = []
    for col in sorted(positions.keys()):
        column_nodes = [val for _, val in sorted(positions[col])]
        result.append(column_nodes)

    return result

# Приклад 1:
tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
result1 = vertical_order_traversal(tree1)
print("\n Vertical order traversal: ",result1)  

# Приклад 2:
tree2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3))
result2 = vertical_order_traversal(tree2)
print("\n Vertical order traversal: ",result2)  
