class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        prefix = [0] * n

        prefix[0] = stones[0]

        for i in range(1, len(stones)):
            prefix[i] = prefix[i - 1] + stones[i]
        
        res = prefix[n-1]

        for i in range(n-2,0,-1):
            res = max(res,prefix[i]-res)

        return res
    

            
