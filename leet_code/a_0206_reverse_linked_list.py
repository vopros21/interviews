# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.

# Runtime: ms: beats %
# Memory: MB: beats %


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse_list(self, list1):
        """
        :type list1: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


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
