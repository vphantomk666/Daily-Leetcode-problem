class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(nums)
        summ = nums[0]
        for i in range(1,n):
            if nums[i] == nums[i-1]+1:
                summ += nums[i]

            else:
                break
        while summ in seen:
            summ+=1
        
        return summ