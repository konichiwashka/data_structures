class Queue(object):
    def __init__(self):
        self.queue = []

    def appending_item_to_end(self, item):
        self.queue.append(item)

    def appending_to_start(self, item):
        self.queue.insert(0, item)

    def delete_first_item(self):
        if len(self.queue) == 0:
            print("List is empty")
        else:
            self.queue.pop(0)

    def delete_last_item(self):
        if len(self.queue) == 0:
            print("List is empty")
        else:
            self.queue.pop()


my_queue = Queue()
for i in range(1, 10):
    my_queue.appending_item_to_end(i)
for n in range(1, 5):
    my_queue.appending_to_start(n)
for z in range(1, 4):
    my_queue.delete_first_item()
for x in range(1, 5):
    my_queue.delete_last_item()
print(my_queue)
