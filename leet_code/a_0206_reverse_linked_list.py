# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.

# Runtime: 65ms: beats 5.43%
# Memory: 17.8MB: beats 67.28%

from ListNode import ListNode
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverse_list(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = None
        while head is not None:
            node = head
            head = node.next
            if result is None:
                result = node
                result.next = None
            else:
                node.next = result
                result = node
        return result


if __name__ == "__main__":
    list_a = ListNode(1, ListNode(2, ListNode(4)))
    # list_a = ListNode(2)
    # list_b = ListNode(1)
    # list_a = None
    # list_b = None
    list_a = Solution.reverse_list(Solution(), list_a)
    while list_a:
        print(list_a.val)
        list_a = list_a.next
