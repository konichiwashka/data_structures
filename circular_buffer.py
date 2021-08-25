class Queue(object):
    def __init__(self):
        self.queue = [[]]*9
        self.pointer_start = 0
        self.pointer_end = 0

    def appending_item(self, item):
        self.queue[self.pointer_end] = item
        self.pointer_end += 1
        self.pointer_end = self.pointer_end % 9
        self.pointer_start = self.pointer_end

    def delete_item(self):
        if len(self.queue) == 0:
            print("List is empty")
        else:
            self.queue[self.pointer_start] = []
            self.pointer_start += 1


my_queue = Queue()
for i in range(1, 15):
    my_queue.appending_item(i)
my_queue.delete_item()
my_queue.delete_item()
my_queue.delete_item()
my_queue.delete_item()
my_queue.appending_item(100)
my_queue.appending_item(200)
my_queue.appending_item(300)
my_queue.appending_item(400)
my_queue.appending_item(500)
my_queue.appending_item(600)
my_queue.delete_item()
print(my_queue)
