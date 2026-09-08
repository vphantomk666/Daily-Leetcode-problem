class Solution:
    def countCommas(self, n: int) -> int:
        res = 0

        lower = 1000

        commas = 1

        while lower <= n:
            upper = lower*1000-1
            if upper > n : upper = n
            countcommas = upper-lower +1
            res += (countcommas*commas)

            lower *= 1000
            commas += 1
        
        return res
