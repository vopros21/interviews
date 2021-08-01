"""
Source lection: https://youtu.be/qf82-r9hl2Y
"""


def hoare_sort(original):
    original_len = len(original)
    if original_len <= 1:
        return
    barrier = original[0]
    left = []
    middle = []
    right = []
    for x in original:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    hoare_sort(left)
    hoare_sort(right)
    k = 0
    for x in left + middle + right:
        original[k] = x
        k += 1
