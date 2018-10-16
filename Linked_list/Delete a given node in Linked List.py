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

def deleteNode1 (head, node):
    dummy_node = LinkedListNode(0)
    dummy_node.next = head
    prev, curr = dummy_node, head
    while curr and curr != node:
        prev = prev.next
        curr = curr.next
    if curr != None:
        prev.next = curr.next
    return dummy_node.next

for target in xrange(8):
    head = create_linked_list([1,3,6,13,31,52,8])
    target_node = head
    while target != 0:
        target -= 1
        target_node = target_node.next
    # printLinked_list(head)
    printLinked_list(deleteNode1(head, target_node))

