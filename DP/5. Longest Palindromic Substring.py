# coding=utf-8


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