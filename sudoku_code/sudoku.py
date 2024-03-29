# Given an incomplete Sudoku configuration in terms of a 9 x 9 2-D square matrix
# (mat[][]). The task to print a solved Sudoku. For simplicity you may assume that
# there will be only one unique solution.
#
# Sample Sudoku for you to get the logic for its solution:
#
#
# Input:
# The first line of input contains an integer T denoting the no of test cases.
# Then T test cases follow. Each test case contains 9*9 space separated values
# of the matrix mat[][] representing an incomplete Sudoku state where
# a 0 represents empty block.
#
# Output:
# For each test case, in a new line, print the space separated values of
# the solution of the the sudoku.
#
# Constraints:
# 1 <= T <= 10
# 0 <= mat[] <= 9
#
# Example:
# Input:
# 1
# 3 0 6 5 0 8 4 0 0
# 5 2 0 0 0 0 0 0 0
# 0 8 7 0 0 0 0 3 1
# 0 0 3 0 1 0 0 8 0
# 9 0 0 8 6 3 0 0 5
# 0 5 0 0 9 0 6 0 0
# 1 3 0 0 0 0 2 5 0
# 0 0 0 0 0 0 0 7 4
# 0 0 5 2 0 6 3 0 0
#
# Output: 3 1 6 5 7 8 4 9 2 5 2 9 1 3 4 7 6 8 4 8 7 6 2 9 5 3 1 2 6 3 4 1 5 9 8 7 9 7 4 8 6 3 1 2 5 8 5 1 7 9 2 6 4 3
# 1 3 8 9 4 7 2 5 6 6 9 2 3 5 1 8 7 4 7 4 5 2 8 6 3 1 9
#
# Explanation:
# Testcase 1: The solved sudoku is:
# 3 1 6 5 7 8 4 9 2
# 5 2 9 1 3 4 7 6 8
# 4 8 7 6 2 9 5 3 1
# 2 6 3 4 1 5 9 8 7
# 9 7 4 8 6 3 1 2 5
# 8 5 1 7 9 2 6 4 3
# 1 3 8 9 4 7 2 5 6
# 6 9 2 3 5 1 8 7 4
# 7 4 5 2 8 6 3 1 9
import copy

import numpy as np

# no = int(input('Input number of TCs: '))
no = 1
number = 0
# while number < no:
#     field = []
#     print(f'Input test {number + 1}')
#     for i in range(9):
#         field.append(list(map(int, input().split())))
#     print(*field)
#     flag = True
#     while flag:
#         flag = False
#         for i in range(9):
#             for j in range(9):
#                 top = i - i % 3
#                 bottom = i - i % 3 + 3
#                 left = j - j % 3
#                 right = j - j % 3 + 3
#                 if field[i][j] == 0:
#                     flag = True
#                     row = set(range(1, 10))
#                     for h in range(9):
#                         row.discard(field[i][h])
#                     column = set(range(1, 10))
#                     for k in range(9):
#                         column.discard(field[k][j])
#                     group = set(range(1, 10))
#                     for k in range(top, bottom):
#                         for m in range(left, right):
#                             group.discard(field[k][m])
#                     inter = row.intersection(column.intersection(group))
#                     if len(inter) == 1:
#                         field[i][j] = inter.pop()
#     number += 1
#     for i in range(9):
#         print(*field[i])


def available_numbers(array, x, y):
    row = set(array[x])
    column = set()
    for k in range(9):
        column.add(array[k][y])
    top = x - x % 3
    left = y - y % 3
    group = set()
    for ver in range(top, top + 3):
        for hor in range(left, left + 3):
            group.add(array[ver][hor])
    row.discard(0)
    column.discard(0)
    group.discard(0)
    return intersection(row, column, group)


def intersection(set_1: set, set_2: set, set_3: set) -> set:
    result = set(range(1, 10))
    set_1.update(set_2)
    set_1.update(set_3)
    for el in set_1:
        result.discard(el)
    return result


def sudoku(original):
    flag = False
    current = copy.deepcopy(original)
    for i in range(9):
        for j in range(9):
            cur = current[i][j]
            if cur == 0:
                numbers = available_numbers(current, i, j)
                for k in numbers:
                    current[i][j] = k
                    if not flag:
                        current, flag = sudoku(current)
            if [i, j] == [8, 8]:
                flag = True
    return current, flag


while number < no:
    field = []
    common_line = []
    file = open('../data/sudoku_tests.txt', 'r', encoding='UTF-8')
    for i in range(9):
        line = list(map(int, file.readline().split()))
        field.append(line)
        common_line += line
    res, is_solved = sudoku(field)
    print(is_solved)
    for i in range(9):
        print(*res[i])
    number += 1
print('End of calculations!')
