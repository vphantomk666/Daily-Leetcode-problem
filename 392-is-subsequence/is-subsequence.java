import java.util.Arrays;

class Solution {

    int[][] dp;

    int LCS(String a, String b, int i, int j) {

        if (i == 0 || j == 0) {
            return 0;
        }

        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        if (a.charAt(i - 1) == b.charAt(j - 1)) {
            dp[i][j] = 1 + LCS(a, b, i - 1, j - 1);
        }

        else {
            dp[i][j] = Math.max(
                LCS(a, b, i - 1, j),
                LCS(a, b, i, j - 1)
            );
        }

        return dp[i][j];
    }

    public boolean isSubsequence(String s, String t) {

        int m = s.length();
        int n = t.length();

        dp = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            Arrays.fill(this.dp[i], -1);
        }

        return LCS(s, t, m, n) == m;
    }
}