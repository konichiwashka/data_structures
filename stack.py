from queue_example import Queue


class Stack(Queue):
    def appending_item(self, item):
        self.queue.append(item)

    def delete_item(self):
        assert len(self.queue) != 0, 'Empty queue'
        self.queue = self.queue[:-1]


my_queue = Stack()
for i in range(1, 10):
    my_queue.appending_item(i)
my_queue.delete_item()
my_queue.delete_item()
print(my_queue)
