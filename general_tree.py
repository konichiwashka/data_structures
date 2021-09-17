class General_tree(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def insert(self, data):
        if self.data in None:
            data = General_tree(data)
        else:
            self.children.append(data)
