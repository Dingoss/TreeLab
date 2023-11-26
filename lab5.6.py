class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    def max_path_sum_helper(node):
        nonlocal max_sum
        if not node:
            return 0

        left_sum = max(max_path_sum_helper(node.left), 0)
        right_sum = max(max_path_sum_helper(node.right), 0)

        max_sum = max(max_sum, node.val + left_sum + right_sum)

        return node.val + max(left_sum, right_sum)

    max_sum = float('-inf')
    max_path_sum_helper(root)
    return max_sum

# Приклад 1
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
result1 = max_path_sum(tree1)
print("\n Max path:",result1)  

# Приклад 2
tree2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
result2 = max_path_sum(tree2)
print("\n Max path:",result2)  
