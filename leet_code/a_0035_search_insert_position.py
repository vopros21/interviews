# https://leetcode.com/problems/search-insert-position/

# Runtime: 61ms: beats 73.24%
# Memory: 17MB: beats 82.41%

from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0
        while left <= right:
            if target <= nums[left]:
                return left
            if target > nums[right]:
                return right + 1
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return middle


if __name__ == '__main__':
    numbers = [1, 3, 5, 6]
    for i in range (10):
        print(i , ": ", Solution().search_insert(nums=numbers, target=i))
