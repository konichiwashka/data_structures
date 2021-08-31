class CB(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cb = [None] * capacity
        self.pointer_start = 0
        self.pointer_end = 0
        self.count = 0

    def appending_item(self, item):
        self.cb[self.pointer_end] = item
        self.pointer_end += 1
        self.count += 1
        self.pointer_end = self.pointer_end % self.capacity
        if self.count > self.capacity:
            self.pointer_start = self.pointer_end
        else:
            self.pointer_start = 0

    def delete_item(self):
        assert len(self.cb) != 0, 'Empty queue'
        self.cb[self.pointer_start] = None
        self.pointer_start += 1

    def print_out(self):
        return self.cb



