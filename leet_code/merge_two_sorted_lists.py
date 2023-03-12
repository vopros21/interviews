# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.

# Runtime: 20ms: beats 83,88%
# Memory: 13.7MB: beats 13.96%


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            beginning = list1
            list1 = list1.next
        else:
            beginning = list2
            list2 = list2.next
        temp = beginning
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next
        if not list1:
            temp.next = list2
        elif not list2:
            temp.next = list1
        return beginning


if __name__ == "__main__":
    list_a = ListNode(1, ListNode(2, ListNode(4)))
    list_b = ListNode(1, ListNode(3, ListNode(4)))
    # list_a = ListNode(2)
    # list_b = ListNode(1)
    # list_a = None
    # list_b = None
    list_a = Solution.mergeTwoLists(Solution(), list_a, list_b)
    while list_a:
        print(list_a.val)
        list_a = list_a.next
