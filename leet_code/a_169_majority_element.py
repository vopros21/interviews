# https://leetcode.com/problems/majority-element/
# Runtime: ms: beats %
# Memory: MB: beats %

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            res[i] = res.get(i, 0) + 1
        return max(res, key=res.get)


if __name__ == '__main__':
    numbers = [3, 1, 3, 2, 1]
    print(Solution().majorityElement(numbers))
