class CB(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.pointer_start = 0
        self.pointer_end = 0
        self.count = 0

    def appending_item(self, item):
        self.queue[self.pointer_end] = item
        self.pointer_end += 1
        self.count += 1
        self.pointer_end = self.pointer_end % self.capacity
        if self.count > self.capacity:
            self.pointer_start = self.pointer_end
        else:
            self.pointer_start = 0

    def delete_item(self):
        assert len(self.queue) != 0, 'Empty queue'
        self.queue[self.pointer_start] = None
        self.pointer_start += 1


my_queue = CB(9)
for i in range(1, 10):
    my_queue.appending_item(i)
my_queue.delete_item()
for z in range(1, 5):
    my_queue.appending_item(z*100)
my_queue.delete_item()
print(my_queue)
