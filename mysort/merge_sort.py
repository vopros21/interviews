"""
Source lection: https://youtu.be/qf82-r9hl2Y
"""


def merge(first_list: list, second_list: list):
    fl_len = len(first_list)
    sl_len = len(second_list)
    list_result = [0] * (fl_len + sl_len)
    i = k = n = 0
    while i < fl_len and k < sl_len:
        if first_list[i] <= second_list[k]:
            list_result[n] = first_list[i]
            i += 1
        else:
            list_result[n] = second_list[k]
            k += 1
        n += 1
    while i < fl_len:
        list_result[n] = first_list[i]
        i += 1
        n += 1
    while k < sl_len:
        list_result[n] = second_list[k]
        k += 1
        n += 1
    return list_result


def merge_sort(original: list):
    original_len = len(original)
    if original_len <= 1:
        return
    middle = original_len // 2
    left = [original[i] for i in range(middle)]
    right = [original[i] for i in range(middle, original_len)]
    merge_sort(left)
    merge_sort(right)
    merged = merge(left, right)
    for i in range(original_len):
        original[i] = merged[i]
