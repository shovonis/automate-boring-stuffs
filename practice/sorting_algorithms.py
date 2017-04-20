_author_ = "Rifatul Islam"

"""Insertion sort algorithm Implementation"""


def insertion_sort(items):
    for index in range(1, len(items)):
        key = items[index]
        i = index - 1

        while i >= 0 and items[i] > key:
            items[i + 1] = items[i]
            items[i] = key
            i -= 1


number_list = [5, 4, 2, 1, 5, 6]
insertion_sort(number_list)
print(number_list)
