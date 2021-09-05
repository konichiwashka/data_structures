import random
from bubble_sort import bubble_sort


def bucket_sort_true(my_list, n):
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
    print(bucket)
    for x in range(n):
        bubble_sort(bucket[x-1])
    print(bucket)


my_list = [random.randint(1, 50) for x in range(1, 21)]
bucket_sort_true(my_list, 5)
dsf