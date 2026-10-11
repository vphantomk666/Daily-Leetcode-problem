class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        nums.insert(0,0)
        n = len(nums)
        res = 0
        for i in range(1,n):
            if (n-1)%i == 0:
                res += nums[i]*nums[i]
            
        return res