from collections import deque, defaultdict


class Solution(object):
    def buildGraph(self, edges):
        graph = defaultdict(set)
        for pair in edges:
            start, end = pair
            graph[start].add(end)
        return graph

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # BFS:
        graph = self.buildGraph(prerequisites)
        in_degree = [0] * numCourses
        for pair in prerequisites:
            start, end = pair
            in_degree[end] += 1

        queue = deque([])
        finished = [False] * numCourses
        for i in xrange(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        # print queue, graph
        while queue:
            curr_course = queue.popleft()
            finished[curr_course] = True
            # print queue, graph[curr_course]
            for ngb in graph[curr_course]:
                if not finished[ngb]:
                    in_degree[ngb] -= 1
                    if in_degree[ngb] == 0:
                        queue.append(ngb)
        # print finished
        return finished == [True] * numCourses