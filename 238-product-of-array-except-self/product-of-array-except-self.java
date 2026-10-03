class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        int perfix = 1;

        int[] ans = new int[n];

        for(int i = 0; i < n; i++){
            ans[i] = perfix;
            perfix *= nums[i];
        }
        int suffix = 1;
        for(int i = n-1; i >= 0; i--){
            ans[i] *= suffix;
            suffix *= nums[i];
        }

        return ans;

    }
}