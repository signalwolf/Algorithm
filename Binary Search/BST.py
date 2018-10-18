# coding=utf-8

# 不要忘记了initial node 的方法
from random import randint
class BSTNode(object):
    def __init__(self, val):
        self.val = val
        self.left= None
        self.right = None



def insert_BST(root, val):
    if root == None: return None

    if root.val > val and not root.left:
        root.left = BSTNode(val)
    elif root.val > val and root.left:
        insert_BST(root.left, val)
    elif root.val < val and root.right:
        insert_BST(root.right, val)
    elif root.val < val and not root.right:
        root.right = BSTNode(val)


def buildBST(arr, start, end):
    if start >= end: return None
    if start == end - 1: return BSTNode(arr[start])
    mid = start + (end - start ) / 2
    root = BSTNode(arr[mid])
    root.left = buildBST(arr, start, mid)
    root.right = buildBST(arr, mid + 1, end)
    return root

def inorder_traversal(root):
    if root == None: return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def main():
    lens = 20
    ans = set()
    for i in xrange(lens):
        ans.add(randint(0, 100))
    arr = sorted(list(ans))
    root = buildBST(arr, 0, len(arr) - 1)

    for i in xrange(10):
        insert_val = randint(0, 100)
        if insert_val not in ans:
            insert_BST(root, insert_val)
            print insert_val, inorder_traversal(root)

    print sorted(inorder_traversal(root)) == inorder_traversal(root)





if __name__ == '__main__' :
    main()