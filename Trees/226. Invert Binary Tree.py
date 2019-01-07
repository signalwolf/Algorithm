# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        currLevel = [root]
        while currLevel:
            nextLevel = []
            for node in currLevel:
                if node.right:
                    nextLevel.append(node.right)
                if node.left:
                    nextLevel.append(node.left)
                node.left, node.right = node.right, node.left
            currLevel = nextLevel
        return root