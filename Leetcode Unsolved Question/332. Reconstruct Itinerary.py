# coding=utf-8
# coding=utf-8

# sounds like an topological sort, because you must go to one city then you can move to another city,
# shouldn't normal graph can resolve the problem? Greedy select the smallest order node.

# The biggest challenge is the graph have cycle.

# 这是一个Eulerian path （一笔画）的问题。Details： Hierholzer's algorithm
# reference： https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/

from collections import defaultdict
class Solution(object):

    def buildGraph(self, tickets):
        graph = defaultdict(list)
        # 首先在这里需要注意的是让它sorted，这样当我们处理neighbor的时候
        # 一定是按照sorted order在遍历
        for pair in sorted(tickets):
            start, end = pair
            graph[start].append(end)
        return graph

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        def dfs(node):
            # DFS遍历整个graph，当route的lens第一次等于ticket + 1的长度时
            # 表明找到了node
            # 严格按照DFS的要求来，每次访问一个点然后将其加入到route中，此时看它
            # 是否有neighbor可走，如果不可继续直接返回
            # 在上层node可以看现在的长度是否已经到了，如果没到那么表明这不是answer
            # 那么需要将最后一个pop出来，然后把之前删除的node加回去，然后再继续dfs
            route.append(node)
            if not graph[node]:
                return
            for i, val in enumerate(graph[node]):
                graph[node].pop(i)
                # route.append(new_node)
                dfs(val)
                if len(route) == len(tickets) + 1: return
                graph[node].insert(i, val)
                route.pop()
            # route.pop()
            return

        graph = self.buildGraph(tickets)
        route = []
        dfs('JFK')
        return route

# Better Solution #
class Solution2(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        flight_map = defaultdict(list)
        # 由于后面是pop的，故而在这需要保持reverse的order
        for from_, to in sorted(tickets, reverse=True):
            flight_map[from_].append(to)
        path = []
        # 使用了类似于topological 的办法，但是这个方法太smart了
        # 遇上了估计也想不到

        # idea是这样的，
        # 最后一个到达的node一定是无处可取的点，故而我们先找到这个点
        # 然后除掉她之后再找下一个无处可去的点，这样就解决了这个问题。
        # 每次找的都是无处可去的点，这样便解决了问题。
        def dfs(from_='JFK'):
            while flight_map[from_]:
                dfs(flight_map[from_].pop())
            path.append(from_)
        dfs()
        return path[::-1]
