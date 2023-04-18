# https://leetcode.com/problems/merge-strings-alternately/
# Runtime: 33ms: beats 52.98%
# Memory: 13.9MB: beats 9.46%

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        result = ""
        while i < min(len(word1), len(word2)):
            result += word1[i] + word2[i]
            i += 1
        result += word1[i:]
        result += word2[i:]
        return result


if __name__ == '__main__':
    w1 = "a"
    w2 = "prq"
    print(Solution().mergeAlternately(w1, w2))