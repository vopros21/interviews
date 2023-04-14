# https://leetcode.com/problems/valid-palindrome/

# Runtime: 52ms: beats 44.47%
# Memory: 14.6MB: beats 95.2%

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            char_a = s[i]
            char_z = s[j]
            if not char_a.isalnum():
                i += 1
                continue
            if not char_z.isalnum():
                j -= 1
                continue
            if char_a.lower() != char_z.lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    str_list = [" ", "A man, a plan, a canal: Panama", "race a car"]
    for string in str_list:
        print(Solution().isPalindrome(string))
