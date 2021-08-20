def append_to_start(queue, item):
    queue.insert(0, item)


def append_to_end(queue, item):
    queue.append(item)


def delete_item_in_first_place(queue):
    queue.pop(0)


def delete_item_in_last_place(queue):
    lenght = len(queue) - 1
    queue.pop(lenght)


my_queue = []
for i in range(1, 5):
    append_to_end(my_queue, i)
for z in range(1, 6):
    append_to_start(my_queue, z*2)
for i in range(1, 3):
    delete_item_in_last_place(my_queue)
delete_item_in_first_place(my_queue)
print(my_queue)
