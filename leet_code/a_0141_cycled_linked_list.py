# https://leetcode.com/problems/linked-list-cycle/

# Runtime: 58ms: beats 52.65%
# Memory: 18MB: beats 7.71%

from typing import Optional
from ListNode import ListNode


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
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
    print(Solution().has_cycle(list_a))
