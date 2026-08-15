class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        T = XOR = 0
        for num in nums:
            T |= num>0
            XOR ^= num
        
        return T*(n-(not XOR))

