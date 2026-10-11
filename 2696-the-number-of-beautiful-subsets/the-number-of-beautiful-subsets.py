from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = 0
        freq = defaultdict(int)
        n = len(nums)

        def solve(idx):
            nonlocal res

            if idx == n:
                res += 1
                return

            solve(idx + 1)

            x = nums[idx]

            if freq[x - k] == 0 and freq[x + k] == 0:
                freq[x] += 1
                solve(idx + 1)
                freq[x] -= 1

        solve(0)

        return res - 1
