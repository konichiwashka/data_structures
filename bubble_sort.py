def bubble_sort(my_list):
    n = len(my_list)
    for x in range(n - 1):
        for j in range(n - x - 1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]


my_list = [345, 543, 135, 12, 16, 6, 1325]
bubble_sort(my_list)
