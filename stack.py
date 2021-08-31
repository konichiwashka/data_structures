from queue_example import Queue


class Stack(Queue):
    def appending_item(self, item):
        self.queue.append(item)

    def delete_item(self):
        assert len(self.queue) != 0, 'Empty queue'
        self.queue = self.queue[:-1]



