class Solution:
    def maxSumOfSquares(self, num: int, summ: int) -> str:
        res = ""

        while num > 0:
            curr = min(9,summ)
            res += str(curr)
            summ -= curr
            num -= 1
        
        
        return "" if summ != 0 else res
        
        
        

