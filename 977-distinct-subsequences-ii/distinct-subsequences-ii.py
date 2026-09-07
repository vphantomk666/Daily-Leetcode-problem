class Solution:
    # def solve(self, s: str, n: int, prev: list[int], memo: list[int]) -> int:
        # if n == 0:
        #     return 1

        # if memo[n] != -1:
        #     return memo[n]

        # total = 2 * self.solve(s, n - 1, prev, memo)

        # duplicate = 0

        # if prev[n] != -1:
        #     duplicate = self.solve(s, prev[n] - 1, prev, memo)

        # memo[n] = (total - duplicate) % (10**9 + 7)

        # return memo[n]

    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7

        prev = [-1] * (n + 1)

        last = {}

        for i in range(1, n + 1):
            c = s[i - 1]

            if c in last:
                prev[i] = last[c]

            last[c] = i

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1,n+1):
            total = (2*dp[i-1])%MOD

            if prev[i] != -1:
                duplicates = dp[prev[i]-1]
                total = (total - duplicates + MOD)%MOD
                
            dp[i] = total

        return (dp[n]-1 + MOD) % MOD