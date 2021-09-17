class General_tree(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, data):
        data.parent = self
        self.children.append(data)

    def insert_child(self, node, subtree: list):
        for x in subtree:
            node.add_child(General_tree(x))


def create_node(name_of_subtree, list_of_components):
    name_of_subtree = General_tree(f'{name_of_subtree}')
    root.add_child(name_of_subtree)
    root.insert_child(name_of_subtree, list_of_components)


list_laptop = ['Mac', 'Win', 'Lin']
list_cell_phone = ['Iphone', 'Samsung', 'Xiaomi', 'Huawei']
root = General_tree('Electronics')
create_node('laptop', list_laptop)
create_node('cell phone', list_cell_phone)
