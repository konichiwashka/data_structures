from queue_example import Queue
import time


class Deq(Queue):
    def appending_item_to_end(self, item):
        self.queue.append(item)

    def appending_to_start(self, item):
        self.queue.insert(0, item)

    def delete_first_item(self):
        assert len(self.queue) != 0, 'Empty queue'
        self.queue = self.queue[1:]

    def delete_last_item(self):
        try:
            self.queue = self.queue[:-1]
        except Exception:
            print("DEQ is empty")



