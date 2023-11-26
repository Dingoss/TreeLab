class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if not root:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)

    return root

def print_tree(root):
    if not root:
        return

    print_tree(root.left)
    print(root.val, end=" ")
    print_tree(root.right)


tree1 = TreeNode(4,TreeNode(2, TreeNode(1), TreeNode(3)),TreeNode(7, TreeNode(6), TreeNode(9)))
inverted_tree1 = invert_tree(tree1)
print("Inverted Tree 1:")
print_tree(inverted_tree1)

tree2 = TreeNode(2, TreeNode(1), TreeNode(3))
inverted_tree2 = invert_tree(tree2)
print("\nInverted Tree 2:")
print_tree(inverted_tree2)

tree3 = None
inverted_tree3 = invert_tree(tree3)
print("\nInverted Tree 3:")
print_tree(inverted_tree3)

