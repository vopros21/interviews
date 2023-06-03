# https://leetcode.com/problems/single-number/

# Runtime: 139ms: beats 49.46%
# Memory: 16.7MB: beats 82.56%

from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res


if __name__ == "__main__":
    numbers = [2, 2, 1, 1, 3, 4, 5, 4, 5]
    print(Solution().single_number(numbers))
