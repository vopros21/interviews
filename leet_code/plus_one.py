# https://leetcode.com/problems/plus-one/

# Runtime: 37ms: beats 44.41%
# Memory: 13.8MB: beats 94.43%

from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        k = 0
        for i in range(1, len(digits) + 1):
            k = digits[-i] + 1
            digits[-i] = k % 10
            if k < 10:
                return digits
        if k != 0:
            digits.insert(0, k // 10)
        return digits


if __name__ == "__main__":
    set1 = [1, 2, 3]
    print(Solution().plus_one(digits=set1))
