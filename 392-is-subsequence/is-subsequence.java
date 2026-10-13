class Solution {
    private int[][] dp;

    private int solve(String a, String b, int i, int j) {
        if (i == 0 || j == 0) {
            return 0;
        }

        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        if (a.charAt(i - 1) == b.charAt(j - 1)) {
            dp[i][j] = 1 + solve(a, b, i - 1, j - 1);
        } else {
            dp[i][j] = Math.max(
                solve(a, b, i, j - 1),
                solve(a, b, i - 1, j)
            );
        }

        return dp[i][j];
    }

    public boolean isSubsequence(String s, String t) {
        int m = s.length();
        int n = t.length();

        dp = new int[m + 1][n + 1];

        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        return solve(s, t, m, n) == m;
    }
}