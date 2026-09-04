class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suf = [0] * n
        mn = float('inf')

        for i in range(n - 1, -1, -1):
            mn = min(mn, nums[i])
            suf[i] = mn

        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            if mx - suf[i] <= k:
                return i

        return -1