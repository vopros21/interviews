# https://leetcode.com/problems/excel-sheet-column-title/

# Runtime: ms: beats %
# Memory: MB: beats %

class Solution:
    def convert_to_title(self, column_number: int) -> str:
        count = 0
        index = 0
        for ch in column_title:
            if index != 0:
                count *= 26
            index += 1
            count += int(ch, 36) - 9
        return count


if __name__ == '__main__':
    lines = [1, 2, 26, 27, 28]
    for l in lines:
        print(Solution().convert_to_title(l))