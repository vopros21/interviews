# https://leetcode.com/problems/add-two-numbers/

# Runtime: 65ms: beats 79.31%
# Memory: 14MB: beats 6.60%

from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    @staticmethod
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        tmp = result
        prev = None
        while l1 or l2:
            k = tmp.val
            if l1:
                k += l1.val
                l1 = l1.next
            if l2:
                k += l2.val
                l2 = l2.next
            tmp.val = k % 10
            prev = tmp
            tmp.next = ListNode(k // 10)
            tmp = tmp.next
        if tmp.val == 0:
            prev.next = None
        return result


if __name__ == '__main__':
    # a = ListNode(2, ListNode(4, ListNode(3)))
    # b = ListNode(5, ListNode(6, ListNode(4)))
    # a = b = ListNode(0)
    a = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    b = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    c = Solution().add_two_numbers(a, b)
    while c:
        print(c.val, end='')
        c = c.next
