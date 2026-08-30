class Solution {
    public int minimumDeletions(int[] nums) {
        int n = nums.length;

        int min = nums[0];
        int max = nums[0];

        for (int num : nums) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        int i = -1;
        int j = -1;

        for (int k = 0; k < n; k++) {
            if (nums[k] == min) {
                i = k;
            }

            if (nums[k] == max) {
                j = k;
            }
        }

        int left = Math.min(i, j);
        int right = Math.max(i, j);

        int removeLeft = right + 1;

        int removeRight = n - left;

        int removeBoth = (left + 1) + (n - right);

        return Math.min(removeLeft,
                Math.min(removeRight, removeBoth));
    }
}