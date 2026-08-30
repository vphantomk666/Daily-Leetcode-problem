class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return 1 

        mn = min(nums)
        mx = max(nums)

        l = nums.index(mn)
        r = nums.index(mx)
        
        idx_l = min( l,r )
        idx_r = max( l,r )
        

        del_l = idx_r+1
        del_r = n-idx_l

        del_lr = (idx_l+1)+(n-idx_r)

        return min(del_l, del_r, del_lr)





