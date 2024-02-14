class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)

        balance = self.balance_factor(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        elif key > root.key:
            return self.search(root.right, key)

    def AVL_search(self, key):
        return self.search(self.root, key)


# Example usage:
avl_tree = AVLTree()
keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for key in keys:
    avl_tree.root = avl_tree.insert(avl_tree.root, key)

search_key = 10
result = avl_tree.AVL_search(search_key)

if result:
    print(f"Key {search_key} found in the AVL tree.")
else:
    print(f"Key {search_key} not found in the AVL tree.")
