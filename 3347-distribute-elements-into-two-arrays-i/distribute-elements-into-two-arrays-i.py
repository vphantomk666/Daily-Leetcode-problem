class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr = ([nums[0]],[nums[1]])
        for x in nums[2:]:
            arr[arr[0][-1]<=arr[1][-1]].append(x)
        
        return arr[0]+arr[1]