class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        if len(piles)%2 != 0 or sum(piles) % 2 == 0:
            return False
        
        matrix = [[0]*n for _ in range(n)]
        
        def dp(i:int, j: int) -> None:
            if i == j:
                return piles[i]

            if matrix[i][j] == 0:
                return matrix[i][j]
            
            matrix[i][j] = max(piles[i]- dp(i+1, j), piles[j]-dp(i,j-1))

            return matrix[i][j]

        return dp(0, n-1) >=0

        

