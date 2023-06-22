# https://leetcode.com/problems/excel-sheet-column-title/

# Runtime: ms: beats %
# Memory: MB: beats %

class Solution:
    def convert_to_title(self, column_number: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while column_number > 0:
            result = alphabet[column_number % 26 - 1] + result
            column_number = column_number // 26
        return result


if __name__ == '__main__':
    lines = [1, 2, 26, 27, 28]
    for l in lines:
        print(Solution().convert_to_title(l))