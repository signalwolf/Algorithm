# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head

        slow, fast = head, head.next
        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow != fast: return None

        slow = head
        fast = fast.next
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow