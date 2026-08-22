class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        d_sum = 0
        d_product = 1
        while n:
            digit = n%10
            d_sum += digit
            d_product *= digit
            n //= 10
        
        res = d_sum+d_product
        return num % res == 0
