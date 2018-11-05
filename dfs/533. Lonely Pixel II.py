from collections import defaultdict


class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        count = 0
        dicts = defaultdict(set)
        rows, cols = defaultdict(set), defaultdict(set)
        for i, row in enumerate(picture):
            dicts[tuple(row)].add(i)

        for i in xrange(len(picture)):
            for j in xrange(len(picture[0])):
                if picture[i][j] == 'B':
                    rows[i].add(j)
                    cols[j].add(i)

        #         print rows
        #         print cols
        #         print dicts

        for row in rows:
            if len(rows[row]) != N: continue

            for col in cols:
                if len(cols[col]) != N: continue
                for r in cols[col]:
                    if r in dicts[tuple(picture[row])]:
                        continue
                    else:
                        break
                else:
                    count += 1
        return count