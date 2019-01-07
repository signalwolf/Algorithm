# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def getlen(self, head):
        res = 0
        while head:
            head = head.next
            res += 1
        return res

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        diff = self.getlen(headA) - self.getlen(headB)
        if diff > 0:
            while diff:
                headA = headA.next
                diff -= 1
        else:
            while diff:
                headB = headB.next
                diff += 1

        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
