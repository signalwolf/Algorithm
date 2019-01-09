# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        curr = dummyNode
        heap = []
        for listHead in lists:
            if listHead != None:
                heappush(heap, (listHead.val, listHead))

        while heap:
            # heap pop and heap push to mantain the heap
            currVal, currNode = heappop(heap)
            if currNode.next:
                heappush(heap, (currNode.next.val, currNode.next))

            # build up the merged list:
            curr.next = currNode
            currNode.next = None
            curr = curr.next
        return dummyNode.next


