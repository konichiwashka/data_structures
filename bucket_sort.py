from bubble_sort import bubble_sort


def bucket_sort(my_list, n):
    bucket = [[] for x in range(n)]
    my_list_sorted = []
    var = max(my_list)/n
    z = 0
    if z == n:
        return z
    else:
        for z in range(n):
            bucket[z] = [my_list[x] for x in range(len(my_list)) if (z+1)*var >= my_list[x] >= z*var+1]
    for x in range(n):
        bubble_sort(bucket[x-1])
    for j in range(n):
        my_list_sorted += bucket[j-1]


def bucket_sort_alternative_version(my_list, n):
    bucket = [[] for x in range(n)]
    my_list_sorted = []
    var = max(my_list)/n
    z = 0
    if z == n:
        return z
    else:
        for z in range(n):
            for x in range(len(my_list)):
                if (z+1)*var >= my_list[x] >= z*var+1:
                    bucket[z].append(my_list[x])
    for x in range(n):
        bubble_sort(bucket[x-1])
    for j in range(n):
        my_list_sorted += bucket[j-1]
