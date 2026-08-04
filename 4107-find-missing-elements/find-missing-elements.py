class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = min(nums)
        j = max(nums)

        res = []
        for k in range(i,j):
            if k not in nums:
                res.append(k)


        return res if res else []

