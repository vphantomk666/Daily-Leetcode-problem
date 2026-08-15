class Solution {
    public int longestSubsequence(int[] nums) {
        int xor = 0;
        int n = nums.length;
        boolean nonZero = false;

        for(int num : nums){
            nonZero |= num>0;
            xor ^= num;
        }

        if (!nonZero) return 0;
        return xor==0? n-1 : n;
    }
}