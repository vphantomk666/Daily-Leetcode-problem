class Solution {
    public int minMoves2(int[] nums) {

        Arrays.sort(nums);

        int n = nums.length;
        int res = 0;
        int median = nums[n / 2];

        for (int i = 0; i < n / 2; i++) {
            res += Math.abs(nums[i] - median);
            res += Math.abs(nums[n - i - 1] - median);
        }

        if (n % 2 != 0) {
            res += Math.abs(nums[n / 2] - median);
        }

        return res;
    }
}