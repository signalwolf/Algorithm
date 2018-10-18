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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        left_height, right_height = self.getHeight(root.left), self.getHeight(root.right)
        ans = 1
        if left_height != right_height:
            ans += 2 ** right_height - 1
            ans += self.countNodes(root.left)
        else:
            ans += 2 ** (left_height) - 1
            ans += self.countNodes(root.right)
        return ans

    def getHeight(self, root):
        ans = 0
        while root:
            ans += 1
            root = root.left
        return ans