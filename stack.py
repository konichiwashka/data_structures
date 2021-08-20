def append_item(queue, item):
    queue.append(item)


def delete_item(queue):
    if len(queue) >= 1:
        queue.pop()
    else:
        print("Empty queue")


my_queue = []
for i in range(1, 10):
    append_item(my_queue, i)
for x in range(1, 4):
    delete_item(my_queue)
print(my_queue)
