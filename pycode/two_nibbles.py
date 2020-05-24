# Given a byte, swap the two nibbles in it. For example 100 is be represented
# as 01100100 in a byte (or 8 bits). The two nibbles are (0110) and (0100).
# If we swap the two nibbles, we get 01000110 which is 70 in decimal.
#
# Input:
# The first line contains 'T' denoting the number of testcases. Each testcase contains a single positive integer X.
#
# Output:
# In each separate line print the result after swapping the nibbles.
#
# Constraints:
# 1 ≤ T ≤ 70
# 1 ≤ X ≤ 255
#
# Example:
# Input:
# 2
# 100
# 129
#
# Output:
# 70
# 24

number = int(input('Number of tests: '))
while number > 0:
    number -= 1
    a = int(input('Input number to convert: '))
    bin_a = bin(a)
    str_bin_a = str(bin_a)[2:]
    str_bin_a = ('00000000' + str_bin_a)[-8:]
    str_bin_a = '0b' + str_bin_a[4:] + str_bin_a[:4]
    bin_a = int(str_bin_a, 2)
    print(f'Swapped number for {a} is {bin_a}')
