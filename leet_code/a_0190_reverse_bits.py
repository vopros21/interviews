# https://leetcode.com/problems/reverse-bits/

# Runtime: ms: beats %
# Memory: MB: beats %

class Solution:
    def reverse_bits(self, n: int) -> int:
        r = ""
        i = 0
        while i < 32:
            i += 1
            k = n % 2
            n = n // 2
            r = r + str(k)
        k = int(r, 2)
        return k


if __name__ == '__main__':
    first = 0b11111111111111111111111111111101
    second = Solution().reverse_bits(first)
    print(second == 3221225471)
