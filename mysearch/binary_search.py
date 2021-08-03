import mysort.checking


def left_boundary(array: list, key):
    left = -1
    right = len(array)
    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_boundary(array: list, key):
    left = -1
    right = len(array)
    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] <= key:
            left = middle
        else:
            right = middle
    return right


def search(array: list, key):
    if not mysort.checking.is_sorted(array):
        return None
    left = left_boundary(array, key)
    right = right_boundary(array, key)
    if right - left <= 1:
        return -1
    else:
        return left + 1
