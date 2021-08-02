def is_sorted(original: list, ascending=True):
    """Check if list is sorted with O(n)"""
    sign = 2 * int(ascending) - 1
    for i in range(len(original) - 1):
        if sign * original[i] > sign * original[i+1]:
            return False
    return True
