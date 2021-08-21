def append_to_end(queue, item):
    queue.append(item)


def delete_first_item(queue):
    if len(queue) >= 1:
        queue.pop(0)
    else:
        print("Empty queue")


my_queue = []
for i in range(1, 10):
    append_to_end(my_queue, i)
delete_first_item(my_queue)
delete_first_item(my_queue)
print(my_queue)
