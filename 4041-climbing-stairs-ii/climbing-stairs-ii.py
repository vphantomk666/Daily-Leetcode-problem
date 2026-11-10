class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [-1] * (n + 1)

        def solve(i):
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            ans = float('inf')

            for jump in range(1, 4):
                j = i + jump

                if j <= n:
                    curr = costs[j - 1] + jump**2 + solve(j)
                    ans = min(ans, curr)

            dp[i] = ans
            return dp[i]

        return solve(0)


        