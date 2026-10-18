import java.util.Arrays;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private long[][] PT;

    private long solve(int[] nums) {
        int n = nums.length;

        if (n < 3) {
            return 1;
        }

        int root = nums[0];

        int leftCount = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] < root) {
                leftCount++;
            }
        }

        int[] left = new int[leftCount];
        int[] right = new int[n - 1 - leftCount];

        int l = 0, r = 0;

        for (int i = 1; i < n; i++) {
            if (nums[i] < root) {
                left[l++] = nums[i];
            } else {
                right[r++] = nums[i];
            }
        }

        long x = solve(left);
        long y = solve(right);

        long z = PT[n - 1][left.length];

        return ((x * y) % MOD * z) % MOD;
    }

    public int numOfWays(int[] nums) {
        int n = nums.length;

        PT = new long[n + 1][n + 1];

        for (int i = 0; i <= n; i++) {
            PT[i][0] = 1;
            PT[i][i] = 1;

            for (int j = 1; j < i; j++) {
                PT[i][j] =
                    (PT[i - 1][j - 1] + PT[i - 1][j]) % MOD;
            }
        }

        return (int) ((solve(nums) - 1 + MOD) % MOD);
    }
}
