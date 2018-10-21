# coding=utf-8
from Traverse_recursive import preorder, level
# from collections import deque


# preorder使用的是stack，先将curr.val 压入res中，再将curr.right 压入stakc中（这样stack pop的时候出来的晚）
# 然后再将left压入
def pre_order_stack(root):
    if not root: return []
    stack = [root]
    res = []
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    visited = {}
    stack, res = [], []
    curr = root
    while curr or stack:
        while curr != None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        stack, res = [root], []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return res[::-1]

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildBST(arr, start, end):
    if start >= end: return None
    if start == end - 1: return TreeNode(arr[start])
    mid = start + (end - start ) / 2
    root = TreeNode(arr[mid])
    root.left = buildBST(arr, start, mid)
    root.right = buildBST(arr, mid + 1, end)
    return root

from random import randint

def main():
    lens = 20
    ans = set()
    for i in xrange(lens):
        ans.add(randint(0, 100))
    arr = sorted(list(ans))
    root = buildBST(arr, 0, len(arr) - 1)
    print pre_order_stack(root)

    print preorder(root)
    print level(root)

if __name__ == '__main__' :
    main()

