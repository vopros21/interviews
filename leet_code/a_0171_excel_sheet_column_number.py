# https://leetcode.com/problems/excel-sheet-column-number/

# Runtime: 52ms: beats 19.94%
# Memory: 16.1MB: beats 49.93%

class Solution:
    def title_to_number(self, column_title: str) -> int:
        count = 0
        index = 0
        for ch in column_title:
            if index != 0:
                count *= 26
            index += 1
            count += int(ch, 36) - 9
        return count


if __name__ == '__main__':
    lines = ["A", "B", "C", "AA", "Z"]
    for l in lines:
        print(Solution().title_to_number(l))