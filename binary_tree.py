class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_recursive(self.root, key)

    def insert_recursive(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self.insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self.insert_recursive(current_node.right, key)

    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self.search_recursive(current_node.left, key)
        else:
            return self.search_recursive(current_node.right, key)
        
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(20)

print(bst.search(10))
print(bst.search(15))