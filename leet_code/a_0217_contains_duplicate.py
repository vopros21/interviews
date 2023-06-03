# https://leetcode.com/problems/contains-duplicate/
# Runtime: 543ms: beats 79.35%
# Memory: 31.8MB: beats 28.31%

from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) != len(nums):
            return True
        return False


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(Solution().contains_duplicate(nums))
