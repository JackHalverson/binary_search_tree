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

    def in_order_traversal(self):
        return self.in_order_traversal_recursive(self.root)

    def in_order_traversal_recursive(self, current_node):
        result = []
        if current_node is not None:
            result = self.in_order_traversal_recursive(current_node.left)
            result.append(current_node.key)
            result = result + self.in_order_traversal_recursive(current_node.right)
        return result

    def find_min(self):
        return self.find_min_recursive(self.root)

    def find_min_recursive(self, current_node):
        if current_node is None:
            return None
        elif current_node.left is None:
            return current_node.key
        else:
            return self.find_min_recursive(current_node.left)

    def find_max(self):
        return self.find_max_recursive(self.root)

    def find_max_recursive(self, current_node):
        if current_node is None:
            return None
        elif current_node.right is None:
            return current_node.key
        else:
            return self.find_max_recursive(current_node.right)

    def height(self):
        return self.height_recursive(self.root)

    def height_recursive(self, current_node):
        if current_node is None:
            return 0
        else:
            left_height = self.height_recursive(current_node.left)
            right_height = self.height_recursive(current_node.right)
            return max(left_height, right_height) + 1

    def count_leaves(self):
        return self.count_leaves_recursive(self.root)

    def count_leaves_recursive(self, current_node):
        if current_node is None:
            return 0
        if current_node.left is None and current_node.right is None:
            return 1
        else:
            return self.count_leaves_recursive(current_node.left) + self.count_leaves_recursive(current_node.right)

    def serialize(self):
        return ','.join(map(str, self.in_order_traversal()))

    def deserialize(self, data):
        self.root = None
        for key in map(int, data.split(',')):
            self.insert(key)

# Unit tests
def test_bst():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(3)
    bst.insert(7)
    bst.insert(15)
    bst.insert(30)

    assert bst.search(10) == True
    assert bst.search(15) == True
    assert bst.search(100) == False
    assert bst.in_order_traversal() == [3, 5, 7, 10, 15, 20, 30]
    assert bst.find_min() == 3
    assert bst.find_max() == 30
    assert bst.height() == 3
    assert bst.count_leaves() == 4

    serialized = bst.serialize()
    bst2 = BinarySearchTree()
    bst2.deserialize(serialized)
    assert bst2.in_order_traversal() == [3, 5, 7, 10, 15, 20, 30]

    print("All tests passed.")

test_bst()