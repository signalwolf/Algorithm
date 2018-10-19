from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        def root(node):
            if node not in ids:
                ids[node] = node
                # size[node] = 1
            while ids[node] != node:
                ids[node] = ids[ids[node]]
                node = ids[node]
            return node

        ids = {}
        # size = {}
        for account in accounts:
            name = account[0]
            base_id = tuple(account[:2])
            base_id = root(base_id)
            for i in xrange(2, len(account)):
                curr_email = account[i]
                curr_id = root((name, curr_email))
                if curr_id == base_id:
                    continue
                ids[curr_id] = base_id
                # p, q = base_id, curr_id
                # if size[p] < size[q]:
                #     p, q = q, p
                # ids[p] = q
                # size[q] += size[p]
                # print p, q, ids

        visited = defaultdict(set)
        for id in ids:
            visited[root(id)].add(id[1])

        res = []
        for node in visited:
            res.append([node[0]] + sorted(list(visited[node])))
        return res

