
# Bottom up solution: 24ms
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s: return s in wordDict
        wordDict = set(wordDict)
        dp = [False] * len(s)
        for i in xrange(len(s) - 1, -1, -1):
            if s[i:] in wordDict:
                dp[i] = True
            else:
                for j in xrange(i + 1, len(s)):
                    if dp[j] and s[i:j] in wordDict:
                        dp[i] = True
                        break
        return dp[0]


# Top down solution: 28ms
class Solution(object):

    def dfs(self, s, wordDict, sets):

        if s in sets: return False

        if s in wordDict: return True

        for i in xrange(1, len(s)):
            if s[:i] in wordDict and self.dfs(s[i:], wordDict, sets):
                return True
        sets.add(s)
        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0: return s in wordDict
        return self.dfs(s, set(wordDict), set())