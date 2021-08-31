class Queue(object):
    def __init__(self):
        self.queue = []

    def appending_item(self, item):
        self.queue.append(item)

    def delete_item(self):
        assert len(self.queue) != 0, 'Empty queue'
        print(self.queue[0])
        self.queue = self.queue[:-1]

    def print_out(self):
        return self.queue


