# https://leetcode.com/problems/sqrtx/

# Runtime: 1548ms: beats 23.9%
# Memory: 13.8MB: beats 93.49%

class Solution:
    def my_sqrt(self, x: int) -> int:
        if x < 2:
            return x
        for i in range(x + 1):
            if i * i > x:
                return i - 1


if __name__ == "__main__":
    for variable in range(10):
        print(variable, "\t", Solution().my_sqrt(variable))
