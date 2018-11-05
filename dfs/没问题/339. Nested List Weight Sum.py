class Solution(object):

    def dfs(self, nestedList, depth):
        res = 0
        for list in nestedList:
            if list.isInteger():
                res += list.getInteger() * depth
            else:
                res += self.dfs(list.getList(), depth + 1)
        return res

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.dfs(nestedList, 1)