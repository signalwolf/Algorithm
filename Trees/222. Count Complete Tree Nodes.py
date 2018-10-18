# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    res, stop_flag = 0, False

    def dfs(self, root, height, curr_height):
        if curr_height == height:
            self.res += 1
            return
        elif not root.left or not root.right:
            if root.left: self.res += 1
            self.stop_flag = True
            return
        if not self.stop_flag:
            self.dfs(root.left, height, curr_height + 1)
        if not self.stop_flag:
            self.dfs(root.right, height, curr_height + 1)
        return

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node = root
        left, right = 0, 0
        while node:
            left += 1
            node = node.left
        node = root
        while node:
            right += 1
            node = node.right

        if left == right: return 2 ** left - 1
        self.dfs(root, left, 1)
        return self.res + 2 ** right - 1