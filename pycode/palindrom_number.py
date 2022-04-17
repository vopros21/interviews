# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

def is_palindrome(string):
    if len(string) < 2:
        return True
    flag = False
    for i in range(int(len(string)/2)):
        flag = string[i] == string[-i-1]
    return flag


if __name__ == '__main__':
    x = input("Type your number for palindrome checking: ")
    print(f"Number {x} is a palindrome" if is_palindrom(x) else f"Number {x} is not a palindrome")
