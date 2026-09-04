class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)


        for i in range(n):
            before = max(nums[0:i+1])
            after = min(nums[i:n])
            if(before-after) <=k:
                return i

            
        return -1
