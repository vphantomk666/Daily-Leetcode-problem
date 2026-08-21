from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def lcm(a, b):
            return a // gcd(a, b) * b

        def countsmallercoins(x):
            n = len(coins)
            count = 0

            for mask in range(1, 1 << n):

                common = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        common = lcm(common, coins[i])
                        bits += 1

                        if common > x:
                            break

                if common > x:
                    continue

                if bits % 2 == 1:
                    count += x // common
                else:
                    count -= x // common

            return count

        l = 1
        r = max(coins) * k

        result = -1

        while l <= r:
            mid = l + (r - l) // 2

            if countsmallercoins(mid) >= k:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result