class Solution:
    def canAliceWin(self, n: int) -> bool:

        miss = 55 - n
        unplay = round(sqrt(2*miss))
        return unplay % 2 == 1
        
        

