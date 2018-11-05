# coding=utf-8

# 算法的思路：
#   BST的问题在于说它不存在指向下一个的指针。
#   故而我们就是要建立这个指针来试图解决问题
#   如果想象成为一个linked list的话，那么当前子树的最右节点应该指向父亲节点。idea就是这样

# 当在root node的时候，我们先找到左子树的最右节点然后让其right child = in order的下一个，即root
# 当我们遍历到了叶子节点的时候我们就通过其右指针回到root先，然后再将原先的node 的right 给取消掉

def morris_traversal(root):
    if not root: return []
    curr, prev = root, None
    res = []
    while curr:

        # find the right most child of left subtree
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right != curr and prev.right:
                prev = prev.right

            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                res.append(curr.val)
                curr = curr.right
    return res

def inorder(root):
    if root == None: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

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
    ans1 =  morris_traversal(root)
    ans2 = inorder(root)
    print ans1 == ans2


if __name__ == '__main__' :
    main()