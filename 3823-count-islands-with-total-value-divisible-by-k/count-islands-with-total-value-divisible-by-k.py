from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def close(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0

            if grid[i][j] == 0:
                return 0

            curr = grid[i][j]
            grid[i][j] = 0 

            curr += close(i + 1, j)
            curr += close(i - 1, j)
            curr += close(i, j + 1)
            curr += close(i, j - 1)

            return curr

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total = close(i, j)

                    if total % k == 0:
                        res += 1

        return res