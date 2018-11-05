class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        count = 0
        if len(picture) == 0 or len(picture[0]) == 0: return 0
        # 0: unknown, False: have more than 2,
        row, col = [0] * len(picture), [0] * len(picture[0])
        for i in xrange(len(picture)):
            for j in xrange(len(picture[0])):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1

        for i in xrange(len(row)):
            if row[i] != 1:
                continue
            for j in xrange(len(col)):
                if col[j] != 1:
                    continue
                if picture[i][j] == 'B':
                    count += 1
        return count