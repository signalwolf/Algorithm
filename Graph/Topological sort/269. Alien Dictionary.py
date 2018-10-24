from collections import defaultdict, deque


class Solution(object):

    def compare(self, w1, w2):
        for i in xrange(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                return (w1[i], w2[i])
        return None

    def buildGraph(self, words):
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        for i in xrange(len(words) - 1):
            compare_res = self.compare(words[i], words[i + 1])
            if not compare_res: continue
            start, end = compare_res
            graph[start].add(end)
            in_degree[end] += 1
            if start not in in_degree:
                in_degree[start] = 0
        return graph, in_degree

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph, in_degree = self.buildGraph(words)
        queue = deque()
        for key, val in in_degree.items():
            if val == 0:
                queue.append(key)
        res = ''
        while queue:
            curr = queue.popleft()
            res += curr
            for ngb in graph[curr]:
                if in_degree[ngb] != 0:
                    in_degree[ngb] -= 1
                    if in_degree[ngb] == 0:
                        queue.append(ngb)
        return res



