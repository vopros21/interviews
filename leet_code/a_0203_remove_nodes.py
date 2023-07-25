# https://leetcode.com/problems/remove-linked-list-elements/
# Runtime: 76ms: beats 89.24%
# Memory: 20.14MB: beats 18.98%

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_elements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tmp = head
        prev = head
        while tmp:
            if tmp == head:
                if tmp.val == val:
                    head = head.next
                    tmp = head
                    prev = head
                else:
                    tmp = head.next
                continue
            if tmp.val == val:
                prev.next = tmp.next
                tmp = tmp.next
                continue
            if tmp:
                prev = tmp
                tmp = tmp.next
        return head


if __name__ == '__main__':
    # list_a = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    list_a = ListNode(6, ListNode(6, ListNode(6, ListNode(6))))
    # list_a = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    list_a = Solution().remove_elements(list_a, 6)
    while list_a:
        print(list_a.val)
        list_a = list_a.next
