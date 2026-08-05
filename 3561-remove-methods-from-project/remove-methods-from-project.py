from collections import defaultdict, deque

class Solution:
    def dfs(self, node, invoke, vis):
        queue = deque()
        vis[node] = 1
        queue.append(node)
        while queue:
            v = queue.popleft()
            for nxt in invoke[v]:
                if not vis[nxt]:
                    vis[nxt] = 1
                    queue.append(nxt)

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        invoke = defaultdict(list)
        for u, v in invocations:
            invoke[u].append(v)

        vis = [0] * n
        self.dfs(k, invoke, vis)

        rem = []

        for u, v in invocations:
            if not vis[u] and vis[v]:
                return list(range(n))

        for i in range(n):
            if not vis[i]:
                rem.append(i)

        return rem