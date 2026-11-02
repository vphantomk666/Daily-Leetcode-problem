class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = n//2
        res = 0
        for i in range(mid):
            res += abs(nums[i] - nums[mid])

            res += abs(nums[n-i-1] - nums[mid])

        
        return res