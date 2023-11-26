class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_camera_cover(root):
    def dfs(node):
        nonlocal result
        if not node:
            return 2 

        left_state = dfs(node.left)
        right_state = dfs(node.right)

        if left_state == 0 or right_state == 0:
            result += 1  
            return 1  
        elif left_state == 1 or right_state == 1:
            return 2  
        else:
            return 0  

    result = 0
    if dfs(root) == 0:
        result += 1  
    return result

# Приклад 1:
tree1 = TreeNode(0, None, TreeNode(0, None, TreeNode(0)))
result1 = min_camera_cover(tree1)
print("\nMin camera cover =", result1)  

# Приклад 2:
tree2 = TreeNode(0, None, TreeNode(0, None, TreeNode(0, None, TreeNode(0))))
result2 = min_camera_cover(tree2)
print("\nMin camera cover =", result2)  

# Приклад 3:
tree3 = TreeNode(0, TreeNode(0, None, TreeNode(0, None, TreeNode(0))),None)
result3 = min_camera_cover(tree3)
print("\nMin camera cover =", result3)
