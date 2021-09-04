class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_left(self, new_val):
        if self.left is None:
            self.left = Node(new_val)
        else:
            new_node = Node(new_val)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, new_val):
        if self.right is None:
            self.right = Node(new_val)
        else:
            new_node = Node(new_val)
            new_node.right = self.right
            self.right = new_node
    