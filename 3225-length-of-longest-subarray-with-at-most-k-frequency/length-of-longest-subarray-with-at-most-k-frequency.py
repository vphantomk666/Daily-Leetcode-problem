class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n, max_len=len(nums), 0
        freq=defaultdict(int)
        l=0
        for r, x in enumerate(nums):
            freq[x]+=1
            while freq[x]>k:
                freq[nums[l]]-=1
                l+=1
            max_len=max(max_len, r-l+1)
        return max_len