# coding=utf-8

# stack 解决：


# recursion 解决：超时
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # print preorder
        if len(preorder) <= 2: return True
        base = preorder[0]

        # no left condition
        smaller = False if preorder[1] > base else True

        if preorder[-1] < base:
            index = len(preorder)
        else:
            index = 1

        for i in xrange(1, len(preorder)):
            if preorder[i] > base and preorder[i - 1] < base:
                index = i
                smaller = False
            if (smaller and preorder[i] > base) or (not smaller and preorder[i] < base):
                return False
        return self.verifyPreorder(preorder[1:index]) and self.verifyPreorder(preorder[index:])
