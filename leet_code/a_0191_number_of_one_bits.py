# https://leetcode.com/problems/number-of-1-bits/

# Runtime: 45ms: beats 34.12%
# Memory: 16.3MB: beats 22.46%

class Solution:
    def hammingWeight(self, n: int) -> int:
        # return sum( [n&(1<<i)>0 for i in range(32)] )
        c = 0
        while n > 0:
            c += n % 2
            n = n // 2
        return c