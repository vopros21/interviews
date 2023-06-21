# https://leetcode.com/problems/add-binary/
# Runtime: 54ms: beats 34.32%
# Memory: 16.4MB: beats 38.99%


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        a_int, b_int = int(a, 2), int(b, 2)
        return str(bin(a_int + b_int))[2:]


if __name__ == '__main__':
    s1 = "11"
    s2 = "1"
    print(Solution().add_binary(s1, s2))