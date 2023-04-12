

class Solution:
    def climb_stairs(self, n: int) -> int:
        return n // 2 + 1




if __name__ == "__main__":
    number = 4
    print(Solution().climb_stairs(number))
