class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0

        
        def isConnected(grid, row, col):
            
            row_count = sum(grid[row][j] for j in range(m))
            col_count = sum(grid[i][col] for i in range(n))

            return row_count > 1 or col_count > 1
            

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1 and isConnected(grid, i, j):
                    cnt += 1
        

        return cnt