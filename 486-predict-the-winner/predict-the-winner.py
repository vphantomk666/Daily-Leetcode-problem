from functools import cache
class Solution:
    @cache
    def dp(self, i:int, j:int) -> int:
        if i == j : return self.nums[i]
        
        pickLeft = self.nums[i] - self.dp(i+1, j)
        pickRight = self.nums[j] - self.dp(i, j-1)

        return max(pickLeft, pickRight)

        
    def predictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        n = len(nums)
        if ~n&1 :
            return True
        
        return self.dp(0, n-1) >= 0

        