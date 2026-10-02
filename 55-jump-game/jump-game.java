class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;

        int max_jump = 0;
        for(int i = 0; i<n; i++){
            if (max_jump < i){
                return false;
            }
            max_jump = Math.max(max_jump, i+nums[i]);
            if (max_jump >= n-1){
                return true;
            }
        }

        return false;

        }
}