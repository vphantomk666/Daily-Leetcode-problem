class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def close(i,j):
            if not(0 <= i < m and 0 <= j < n):
                return False
            if grid[i][j]:
                return True
            
            grid[i][j] = 1

            return close(i+1,j) & close(i-1, j) & close(i,j+1) & close(i, j-1)
        

        return sum(close(i,j) for i in range(m) for j in range(n) if not grid[i][j])
