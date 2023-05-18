# https://leetcode.com/problems/can-place-flowers/

# Runtime: 155ms: beats 95.54%
# Memory: 14.3MB: beats 94.1%

from typing import List


class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flag = True
        len_fb = len(flowerbed)
        for i in range(0, len_fb):
            if flowerbed[i] == 1:
                flag = False
                continue
            elif not flag:
                flag = True
                continue
            elif i == len_fb - 1 or flowerbed[i+1] == 0:
                n -= 1
                if n == 0:
                    return True
                flag = False
        return False


if __name__ == "__main__":
    fb = [0, 0, 1, 0, 0, 1, 1, 0]
    # fb = [0]
    num = 2
    print(Solution().can_place_flowers(flowerbed=fb, n=num))
    num = 3
    print(Solution().can_place_flowers(flowerbed=fb, n=num))
