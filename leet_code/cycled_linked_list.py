# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional


# Runtime: 58ms: beats 52.65%
# Memory: 18MB: beats 7.71%


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s = set()
        node = head
        while node.next:
            if node in s:
                return True
            s.add(node)
            node = node.next
        return False


if __name__ == '__main__':
    k = ListNode(1)
    # m = ListNode(2)
    # n = ListNode(0)
    # l = ListNode(-4)
    # k.next = m
    # m.next = n
    # n.next = l
    # l.next = m
    list_a = k
    print(Solution().hasCycle(list_a))
