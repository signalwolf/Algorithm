# coding=utf-8

# 忘了考虑node.val的值为负数的情况
# 算法很简单，就是我考虑两种情况，一种是需要用 root.val的情况
# 这样左边 + 中间 + 右边就是当前root的ans
# 另一种是我左边的结果，我右边的结果更大，这样回复更大的就好。
# 同时向上传输的一定是包含了root的path

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = -float('inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.ans

    def helper(self, root):
        left, right = -float('inf'), -float('inf')
        if root.left: left = self.helper(root.left)
        if root.right: right = self.helper(root.right)
        curr = max(left, 0) + root.val + max(right, 0)
        self.ans = max(self.ans, curr, left, right)
        return max(left, right, 0) + root.val
