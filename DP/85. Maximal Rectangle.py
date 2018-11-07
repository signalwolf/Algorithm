class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[[0 for _ in xrange(2)] for _ in xrange(N)] for _ in xrange(M)]
        top = [[0 for _ in xrange(N)] for _ in xrange(M)]
        left = [[0 for _ in xrange(N)] for _ in xrange(M)]

        dp[0][0] = [1, 1] if matrix[0][0] == '1' else [0, 0]
        top[0][0] = 1 if matrix[0][0] == '1' else 0
        left[0][0] = 1 if matrix[0][0] == '1' else 0

        res = 0
        for i in xrange(1, M):
            if matrix[i][0] == '1':
                dp[i][0][0] = dp[i - 1][0][0] + 1
                top[i][0] = top[i - 1][0] + 1
                left[i][0] = 1
                res = max(dp[i][0][0] * dp[i][0][1], res)

        for j in xrange(1, N):
            if matrix[0][j] == '1':
                dp[0][j][1] = dp[0][j - 1][1] + 1
                left[0][j] = left[0][j - 1] + 1
                top[0][j] = 1
            res = max(dp[0][j][0] * dp[0][j][1], res)

        for i in xrange(1, M):
            for j in xrange(1, N):
                if matrix[i][j] == '1':
                    dp[i][j][0] = min(dp[i - 1][j - 1][0] + 1, top[i - 1][j])
                    dp[i][j][1] = min(dp[i - 1][j - 1][1] + 1, left[i][j - 1])
                    top[i][j] = top[i - 1][j] + 1
                    left[i][j] = left[i][j - 1] + 1
                    res = max(dp[i][j][0] * dp[i][j][1], res, dp[i - 1][j][0] + 1, dp[i][j - 1][1] + 1)

        print top
        print left

        return res