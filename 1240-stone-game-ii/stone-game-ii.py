class Solution:
    
    def stoneGameII(self, piles: List[int]) -> int:
        for i in range(len(piles)-2,-1,-1):
            piles[i] += piles[i+1]
        @cache
        def dp(i,m):
            if i+m*2>=len(piles):
                return piles[i]
            
            return piles[i]-min(dp(i+j,max(m,j)) for j in range(1,m*2+1))
        return dp(0, 1) 