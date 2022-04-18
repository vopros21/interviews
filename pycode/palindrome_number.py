# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


def is_palindrome(x: int) -> bool:
    a = str(x)
    l = len(a)
    for i in range(int(l / 2)):
        if a[i] != a[-i - 1]:
            return False
    return True


if __name__ == '__main__':
    x = int(input("Type your number for palindrome checking: "))
    print(is_palindrome(x))
