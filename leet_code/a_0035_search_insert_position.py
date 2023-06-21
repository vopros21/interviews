# https://leetcode.com/problems/search-insert-position/

# Runtime: ms: beats %
# Memory: MB: beats %

from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            if target > nums[middle]:
                left = middle
            else:
                right = middle


if __name__ == '__main__':
    numbers = [1, 2, 5, 6]
    print(Solution().search_insert(nums=numbers, target=3))
