# https://leetcode.com/problems/isomorphic-strings/

# Runtime: 68ms: beats 16.82%
# Memory: 16.52MB: 81.29beats %

class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d.keys():
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
                continue
            if d[s[i]] != t[i]:
                return False
        return True


if __name__ == '__main__':
    s1 = ["egg", "foo", "paper", "badc"]
    s2 = ["add", "bar", "title", "baba"]
    for i in range(len(s1)):
        print(Solution().is_isomorphic(s1[i], s2[i]))
