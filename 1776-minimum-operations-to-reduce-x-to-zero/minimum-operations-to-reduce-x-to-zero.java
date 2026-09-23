class Solution {
    public int minOperations(int[] nums, int x) {
        int sum = Arrays.stream(nums).sum();

        int target = sum - x;

        if (target < 0){
            return -1;
        }

        if (target == 0){
            return nums.length;
        }

        int l = 0;
        int curr = 0;
        int max_len = 0;

        for(int r = 0; r < nums.length; r++){
            curr += nums[r];

            while (curr > target && l <= r){
                curr -= nums[l];
                l++ ;
            }

            if ( curr == target){
                max_len = Math.max(max_len, r-l+1);
            }
        }

        if (max_len == 0){
            return -1;
        }
        
        return nums.length - max_len;
        
    }
}