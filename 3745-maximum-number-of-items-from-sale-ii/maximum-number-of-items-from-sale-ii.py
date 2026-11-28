class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = {}
        cheapest_price = float('inf')
        for f, p in items:
            freq[f] = freq.get(f, 0) + 1
            cheapest_price = min(cheapest_price, p)

        factor_sum = [0]*(n+1)
        for f in range(1,n+1):
            for k in range(0,n+1,f):
                factor_sum[f] += freq.get(k, 0)
            
        units = []

        for f, p in items:
            cnt = factor_sum[f]-1

            if cnt>0 and p <  2*cheapest_price:
                units.append([p, cnt])
        

        units.sort(key= lambda x: x[0])

        result = 0

        for p, f in units:
            k = min(f, budget//p)

            budget -= k*p

            result += 2*k

        result += budget//cheapest_price

        return result