# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Runtime: 52ms: beats 9.24%
# Memory: 13.8MB: beats 59.32%


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def delete_duplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        beginning = head
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return beginning


if __name__ == "__main__":
    # list_a = ListNode(1, ListNode(1, ListNode(2)))
    list_a = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    list_a = Solution.delete_duplicates(Solution(), list_a)
    while list_a:
        print(list_a.val)
        list_a = list_a.next
