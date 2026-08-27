class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]- points[j][0]) + abs(points[i][1]- points[j][1])

                adj[i].append((j, dist))
                adj[j].append((i, dist))

        def prims_algo(adj, n):
            pq = []

            heapq.heappush(pq, (0, 0))

            inMst = [False]*n
            total_dist = 0
            cnt = 0

            while pq:
                wt, node = heapq.heappop(pq)
                if inMst[node] == True:
                    continue
                
                inMst[node] = True
                total_dist += wt
                cnt += 1

                for nei, nei_wt in adj[node]:
                    if not inMst[nei]:
                        heapq.heappush(pq, (nei_wt, nei))

            return total_dist
            
        return prims_algo(adj, n)
            