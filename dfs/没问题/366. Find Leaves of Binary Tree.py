# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution(object):

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def dfs(root):
            if not root: return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            depth = max(left_depth, right_depth)
            dicts[depth].append(root.val)
            return depth + 1

        dicts = defaultdict(list)
        dfs(root)
        res = []
        for key in sorted(dicts.keys()):
            res.append(dicts[key])
        return res