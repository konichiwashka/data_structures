my_queue = []


def append_item(x):
    my_queue.append(x)


def delete(x):
    for x in range(1, x+1):
        my_queue.pop(0)


for i in range(1, 10):
    append_item(i)
delete(3)
print(my_queue)
