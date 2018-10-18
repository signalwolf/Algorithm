# coding=utf-8

# 我的idea比较简单，就是以每个node为root，然后BFS找到其最远的点并得到height
# 然后如果height小，便update res；如果相同就将当前的root加入到 res中。

# 但是显然有更好的方法，
# 分析问题：很明显对一个tree来说，有两个facts，
#   leaf node的connected node == 1
#   其他的所有的node的connected node 至少为2
# 简化问题：对于一个类似于linked list的tree来说，答案是什么？
#   中点，找到两个leaf node， 然后各自向中间移动，之后遇上了或者是away by one node
#   这个时候便是中点。
# 回归问题：
#   通过简化的问题便知道了，root在两个leaf 的中间。对于任意的tree来说，它的root一定在
#   某两个leaf node 的中点。


# 这个问题可以这样看，如果一个图能够形成一个tree，那么我可以不断的剪掉它的leaf(注意的是
# 它是要一次性将所有的leaf都剪掉)，这样剩下的再形成了一个graph，而此时的中心区域并没有变。
# 的一定是root了，

from collections import deque, defaultdict


class Solution(object):

    def buildGraph(self, pairs):
        dicts = defaultdict(set)
        for pair in pairs:
            a, b = pair
            dicts[a].add(b)
            dicts[b].add(a)
        return dicts

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges: return [0]
        if n == 2: return [0, 1]
        graph = self.buildGraph(edges)
        degree = [0] * n
        for pair in edges:
            degree[pair[0]] += 1
            degree[pair[1]] += 1
        leaves = []
        for i in xrange(n):
            if degree[i] == 1:
                leaves.append(i)

        # leaves = [i if degree[i] == 1 for i in xrange(n)]
        while n > 2:
            n -= len(leaves)
            new_leave = []
            for leaf in leaves:
                ngb = graph[leaf].pop()
                graph[ngb].remove(leaf)
                if len(graph[ngb]) == 1:
                    new_leave.append(ngb)
            leaves = new_leave
        return leaves



class Solution(object):
    def buildGraph(self, pairs):
        dicts = defaultdict(list)
        for pair in pairs:
            a, b = pair
            dicts[a].append(b)
            dicts[b].append(a)
        return dicts

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = self.buildGraph(edges)
        height, res = float('inf'), []
        for i in xrange(n):
            node = i
            visited = [False] * n
            visited[node] = True
            queue = deque([[node, 0]])
            curr_height = 0
            while queue:
                curr, dis = queue.popleft()
                curr_height = max(curr_height, dis)
                for ngb in graph[curr]:
                    if not visited[ngb]:
                        visited[ngb] = True
                        queue.append([ngb, dis + 1])
            if curr_height < height:
                height = dis
                res = [node]
            elif curr_height == height:
                res.append(node)
        return res