class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    if not root:
        return True
    return is_mirror(root.left, root.right)

# Приклад 1
tree = TreeNode(1,TreeNode(2, TreeNode(3), TreeNode(4)),TreeNode(2, TreeNode(4), TreeNode(3)))
print("\nSymmetric?", is_symmetric(tree))  

# Приклад 2
tree = TreeNode(1,TreeNode(2, None, TreeNode(3)),TreeNode(2, None, TreeNode(3)))
print("\nSymmetric?",is_symmetric(tree)) 

# Приклад 3
tree = TreeNode(1,TreeNode(2),TreeNode(1))
print("\nSymmetric?",is_symmetric(tree)) 
