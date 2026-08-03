class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        def dp(i):
            if i >=n:
                return 0

            if memo[i] is not None:
                return memo[i]

            res = float('-inf')
            take = 0
            for j in range(3):
                if i+j < n:
                    take += stoneValue[i+j]
                    res = max(res, take-dp(i+j+1))
            
            memo[i] = res
            return memo[i]
        memo = [None]*n

        score = dp(0)
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        
        return "Tie"
