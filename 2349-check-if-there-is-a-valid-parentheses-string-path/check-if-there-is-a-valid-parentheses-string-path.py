class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2:
            return False

        dp = [[[False] * (m + n)for _ in range(n)]for _ in range(m)]

        cnt = 0

        if grid[0][0] == '(':
            dp[0][0][1] = True
        else:
            return False

        for i in range(m):
            for j in range(n):
                for bal in range(m + n):
                    if not dp[i][j][bal]:
                        continue

                    if j + 1 < n:
                        if grid[i][j + 1] == '(':
                            new_bal = bal + 1
                        else:
                            new_bal = bal - 1

                        if new_bal >= 0:
                            dp[i][j + 1][new_bal] = True

                    if i + 1 < m:
                        if grid[i + 1][j] == '(':
                            new_bal = bal + 1
                        else:
                            new_bal = bal - 1

                        if new_bal >= 0:
                            dp[i + 1][j][new_bal] = True

        return dp[m - 1][n - 1][0]









        # def solve(i, j, cnt):

        #     if i >= m or j >= n:
        #         return False

        #     if cnt < 0:
        #         return False

        #     if (i, j, cnt) in memo:
        #         return memo[(i, j, cnt)]

        #     if grid[i][j] == '(':
        #         cnt += 1
        #     else:
        #         cnt -= 1

        #     if cnt < 0:
        #         return False

        #     if i == m - 1 and j == n - 1:
        #         return cnt == 0

        #     ans = (
        #         solve(i + 1, j, cnt) or
        #         solve(i, j + 1, cnt)
        #     )

        #     memo[(i, j, cnt)] = ans
        #     return ans

        # return solve(0, 0, 0)