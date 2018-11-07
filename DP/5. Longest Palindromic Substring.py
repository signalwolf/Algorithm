# coding=utf-8

# 这道题用DP解不是最优，但是也是一个solution了
# dp[i][j] 代表 s[i : j + 1] 是不是 palindrom,
# 如果是的话，我们就计算器其长度
# 故而 dp[i][j] == True if dp[i + 1][j - 1] is True and s[i] == s[j]

# Better DP solution: 2256 ms
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0] * len(s) for i in range(len(s))]
        ans = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if ans == "" or max_length < j - i + 1:
                        ans = s[i:j + 1]
                        max_length = j - i + 1
        return ans

# my solution: 4972 ms (严重超时)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s

        dp = [[False for _ in xrange(len(s))] for _ in xrange(len(s))]

        # initial
        res, lens, res_len = s[0], len(s), 1
        for i in xrange(len(s)):
            dp[i][i] = True

        diff = 1
        while diff < lens:
            for i in xrange(len(s)):
                j = i + diff
                if j < len(s) and s[i] == s[j] and (dp[i + 1][j - 1] or diff == 1):
                    dp[i][j] = True
                    if j - i + 1 > res_len:
                        res = s[i:j + 1]
                        res_len = j - i + 1
            diff += 1
        return res