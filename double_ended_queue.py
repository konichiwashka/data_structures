from queue_example import Queue
import time


class Deq(Queue):
    def appending_item_to_end(self, item):
        self.queue.append(item)

    def appending_to_start(self, item):
        # 1000 0.003
        # self.queue = [item] + self.queue
        # 1000 0.002
        self.queue.insert(0, item)

    def delete_first_item(self):
        assert len(self.queue) != 0, 'Empty queue'
        self.queue = self.queue[1:]

    def delete_last_item(self):
        try:
            self.queue = self.queue[:-1]
        except Exception:
            print("DEQ is empty")


my_queue = Deq()
for i in range(1, 10):
    my_queue.appending_item_to_end(i)
start_time = time.time()
for n in range(1, 10):
    my_queue.appending_to_start(n)
for z in range(1, 7):
    my_queue.delete_first_item()
for x in range(1, 5):
    my_queue.delete_last_item()
print(my_queue)
print(time.time() - start_time)
