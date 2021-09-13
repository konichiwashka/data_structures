class BinaryTree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinaryTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinaryTree(data)
            else:
                self.right.insert(data)

    def search_data(self, data):
        if self.data == data:
            return True
        else:
            if data < self.data:
                if self.left:
                    return self.left.search_data(data)
                else:
                    return False
            if data > self.data:
                if self.right:
                    return self.right.search_data(data)
                else:
                    return False

    def inorder_traverse(self, node):
        elements_tree = []
        if node:
            elements_tree = (self.inorder_traverse(node.left))
            elements_tree.append(node.data)
            elements_tree = elements_tree + self.inorder_traverse(node.right)
        return elements_tree

    def preorder_traverse(self, node):
        elements_tree = []
        if node:
            elements_tree.append(node.data)
            elements_tree = elements_tree + self.preorder_traverse(node.left)
            elements_tree = elements_tree + self.preorder_traverse(node.right)
        return elements_tree
