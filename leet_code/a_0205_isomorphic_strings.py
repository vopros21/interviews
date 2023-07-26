# https://leetcode.com/problems/isomorphic-strings/

# Runtime: ms: beats %
# Memory: MB: beats %

class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = t[i]
                continue
            if d[s[i]] != t[i]:
                return False
        return True


if __name__ == '__main__':
    s1 = ["egg", "foo", "paper"]
    s2 = ["add", "bar", "title"]
    for i in range(3):
        print(Solution().is_isomorphic(s1[i], s2[i]))
