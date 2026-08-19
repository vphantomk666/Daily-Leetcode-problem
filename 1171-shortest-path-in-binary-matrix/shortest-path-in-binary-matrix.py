from typing import List
import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)

        if m == 0:
            return -1

        n = len(grid[0])

        if n == 0 or grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
            return -1

        directions = [
            (1, 1), (0, 1), (1, 0), (0, -1),
            (-1, 0), (-1, -1), (1, -1), (-1, 1)
        ]

        def isSafe(x, y):
            return 0 <= x < m and 0 <= y < n

        result = [[float('inf')] * n for _ in range(m)]

        pq = []

        heapq.heappush(pq, (0, 0, 0))
        result[0][0] = 0

        while pq:
            d, x, y = heapq.heappop(pq)

            if x == m - 1 and y == n - 1:
                return d + 1

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if isSafe(new_x, new_y) and grid[new_x][new_y] == 0:

                    new_dist = d + 1

                    if new_dist < result[new_x][new_y]:
                        result[new_x][new_y] = new_dist

                        heapq.heappush(
                            pq,
                            (new_dist, new_x, new_y)
                        )

        return -1