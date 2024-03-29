# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].

# Example 2:
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

# Example 3:
#
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
from pprint import pprint

if __name__ == '__main__':
    original_array = input('Input original values, devided by space: ').split()
    for i in range(len(original_array)):
        original_array[i] = int(original_array[i])
    target = int(input('Input target value: '))
    for i in range(len(original_array)):
        a = target - int(original_array[i])
        if a in original_array[i+1:] and original_array.index(a, i + 1) is not i:
            print(i, original_array.index(a, i+1))
            break
