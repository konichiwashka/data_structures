import random
from bubble_sort import bubble_sort
import time


def bucket_sort(my_list, n):
    bucket = [[] for x in range(n)]
    var = max(my_list)/n
    z = 0
    if z == n:
        return z
    else:
        for z in range(n):
            bucket[z] = [my_list[x] for x in range(len(my_list)) if (z+1)*var >= my_list[x] >= z*var+1]
    # print(bucket)
    for x in range(n):
        bubble_sort(bucket[x-1])
    # print(bucket)


def bucket_sort_alternative_version(my_list, n):
    bucket = [[] for x in range(n)]
    var = max(my_list)/n
    z = 0
    if z == n:
        return z
    else:
        for z in range(n):
            for x in range(len(my_list)):
                if (z+1)*var >= my_list[x] >= z*var+1:
                    bucket[z].append(my_list[x])
    # print(bucket)
    for x in range(n):
        bubble_sort(bucket[x-1])
    # print(bucket)


my_list = [random.randint(100, 1000) for x in range(1, 1000)]
res = time.time()
for x in range(100):
    bucket_sort(my_list, 5)
print((time.time()-res)/100)
res1 = time.time()
for x in range(100):
    bucket_sort_alternative_version(my_list, 5)
print((time.time()-res1)/100)

