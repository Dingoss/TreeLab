class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    if not root:
        return "[]"

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    # Вилучаємо всі "null" в кінці списку
    while result and result[-1] == "null":
        result.pop()

    return "[" + ",".join(result) + "]"

def deserialize(data):
    if data == "[]":
        return None

    values = data[1:-1].split(",")
    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


# Приклад 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(5)

serialized1 = serialize(root1)
print("\n Serialized: ",serialized1)  

deserialized1 = deserialize(serialized1)
print("Deserialized: ",serialize(deserialized1)) 

# Приклад 2
root2 = None

serialized2 = serialize(root2)
print("\n Serialized: ",serialized2)  # Виведе "[]"

deserialized2 = deserialize(serialized2)
print("Deserialized: ",serialize(deserialized2))  # Виведе "[]"

# Приклад 3
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(5)

serialized3 = serialize(root3)
print("\n Serialized: ",serialized3) 

deserialized3 = deserialize(serialized3)
print("Deserialized: ",serialize(deserialized3)) 