class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        idx = 0
        cnt = 0
        res = []
        for i in range(len(nums)):
            if nums[i] < target:
                idx += 1
            elif nums[i]== target:
                cnt += 1

        for i in range(cnt):
            res.append(idx+i)

        return  res
        
