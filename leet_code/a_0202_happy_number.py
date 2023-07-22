# https://leetcode.com/problems/happy-number/

# Runtime: 50ms: beats 61.83%
# Memory: 15.99MB: beats 99.95%

class Solution:
    def isHappy(self, n: int) -> bool:
        prev_set = set()
        flag = False
        while n >= 1:
            prev_set.add(n)
            n = Solution().square_sum(n)
            if n == 1:
                flag = True
            if n in prev_set:
                return flag

        return flag

    def square_sum(self, n: int):
        summ = 0
        while n > 0:
            summ += (n % 10) ** 2
            n //= 10
        return summ


if __name__ == '__main__':
    number = 1
    print(Solution().isHappy(number))
