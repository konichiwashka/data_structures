class Queue(object):
    def __init__(self):
        self.queue = []

    def appending_item(self, item):
        self.queue.append(item)

    def delete_item(self):
        if len(self.queue) == 0:
            print("List is empty")
        else:
            self.queue.pop(0)


my_queue = Queue()
for i in range(1, 10):
    my_queue.appending_item(i)
my_queue.delete_item()
my_queue.delete_item()
print(my_queue)
