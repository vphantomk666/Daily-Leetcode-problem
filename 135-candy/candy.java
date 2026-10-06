import java.util.Arrays;

class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;

        int[] child = new int[n];
        Arrays.fill(child, 1);

        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                child[i] = child[i - 1] + 1;
            }
        }

        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                child[i] = Math.max(child[i], child[i + 1] + 1);
            }
        }

        int ans = 0;

        for (int x : child) {
            ans += x;
        }

        return ans;
    }
}