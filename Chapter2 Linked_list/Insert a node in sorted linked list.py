# https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/

# insert by position


class LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(arr):
    dummy_node = LinkedListNode(0)
    prev = dummy_node
    for val in arr:
        curr = LinkedListNode(val)
        prev.next = curr
        prev = curr
    return dummy_node.next

def printLinked_list (head):
    res = []
    while head != None:
        res.append (head.val)
        head = head.next
    print res

def insert(head, val):
    dummy_node = LinkedListNode(0)
    dummy_node.next = head
    prev, curr= dummy_node, head
    # print curr.val, prev.val
    while curr and curr.val < val:
        curr= curr.next
        prev = prev.next
    prev.next = LinkedListNode(val)
    if curr:
        prev.next.next = curr
    return dummy_node.next


head = create_linked_list([1,3,4,7,8,10])
printLinked_list(insert(head, 100))
head = create_linked_list([1,3,4,7,8,10])
printLinked_list(insert(head, 0))
head = create_linked_list([1,3,4,7,8,10])
printLinked_list(insert(head, 5))

# Output:
# [1, 3, 4, 7, 8, 10, 100]
# [0, 1, 3, 4, 7, 8, 10]
# [1, 3, 4, 5, 7, 8, 10]
