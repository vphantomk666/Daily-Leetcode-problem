import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]

        result = [float('inf')] * (n + 1)
        result[k] = 0

        while pq:
            d, node = heapq.heappop(pq)

            if d > result[node]:
                continue

            for neighbor, time in graph[node]:

                new_dist = d + time

                if new_dist < result[neighbor]:
                    result[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        ans = max(result[1:])

        return -1 if ans == float('inf') else ans