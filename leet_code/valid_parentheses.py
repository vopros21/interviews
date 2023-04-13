# https://leetcode.com/problems/valid-parentheses/

# Runtime: 48ms: beats 6.37%
# Memory: 14MB: beats 15.73%

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for s1 in s:
            if s1 in ['(', '[', '{']:
                stack.append(s1)
            else:
                if len(stack) == 0:
                    return False
                elif s1 == ')' and stack.pop() != '(':
                    return False
                elif s1 == ']' and stack.pop() != '[':
                    return False
                elif s1 == '}' and stack.pop() != '{':
                    return False
        if len(stack) != 0:
            return False
        return True