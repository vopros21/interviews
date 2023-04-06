# https://leetcode.com/problems/binary-search/

# Runtime: 238ms: beats 83.14%
# Memory: 15.6MB: beats 13.83%

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            else:
                return middle
        return -1
        # if target in nums:
        #     return nums.index(target)
        # return -1


if __name__ == "__main__":
    numbers = [-1, 0, 3, 5, 9, 12]
    tar = 13
    print(Solution().search(nums=numbers, target=tar))
