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
# insertion_sort(number_list)
# print(number_list)


"""Bubble sort algorithm"""


def bubble_sort(items):
    length = len(items)
    for i in range(length - 1):
        for j in range(length - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


print(bubble_sort(number_list))
