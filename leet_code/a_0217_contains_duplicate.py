# https://leetcode.com/problems/contains-duplicate/
from typing import List


# Runtime: ms: beats %
# Memory: MB: beats %

class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        i = 1
        for n in nums:
            if n in nums[i:]:
                return True
            i += 1
        return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    print(Solution().contains_duplicate(nums))
