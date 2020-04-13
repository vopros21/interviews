# Given a string and number of rows ‘n’. Print the string formed by concatenating n rows when input string is written in row-wise Zig-Zag fashion.
#
# Examples:
# Input:
# str = "ABCDEFGH"
# n = 2
# Output: "ACEGBDFH"
# Explanation: Let us write input string in Zig-Zag fashion in 2 rows.
# A___C___E___G
# __B___D___F___H
# Now concatenate the two rows and ignore spaces
# in every row. We get "ACEGBDFH"
#
# Input:
str = "SPICEITRECRUITMENT"
n = 3
# Output: SEEINPCIRCUTETITRM
# Explanation: Let us write input string in Zig-Zag fashion in 3 rows.
# S_______E_______E_______I_______N
# __P___C___I___R___C___U___T___E___T
# ____I_______T_______R_______M
# Now concatenate the two rows and ignore spaces
# in every row. We get "SEEINPCIRCUTETITRM"
#
# Input:
# The first line of input consists number of the test cases. The description of T test cases is as follows:
# The first line of each test case contains the string, and the second line has 'n' the number of rows.
#
# Output:
# In each separate line print the string after concatenating n rows in a zig zag form.
#
# Constraints:
# 1 ≤ T ≤ 70
# 1 ≤ N ≤ size of string
#
# Example:
# Input:
# 2
# qrrc
# 3
# rfkqyuqfjkxy
# 2
# Output:
# qrcr
# rkyqjxfqufky

# str = input('Input string for work: ')
# n = int(input('Input number of rows: '))
line1 = ''
line2 = ''
line3 = ''
for i, letter in enumerate(str):
    if i % 4 == 0:
        line1 += letter
    elif (i + 1) % 2 == 0:
        line2 += letter
    else:
        line3 += letter
print(line1 + line2 + line3)
