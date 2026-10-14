class Solution {
    static int[] divmod(int a, int b) {
        return new int[]{a / b, a % b};
    }
    public String maxSumOfSquares(int num, int sum) {
        if (sum > 9*num){
            return "";
        }
        int[] result = divmod(sum, 9);
        int q = result[0];
        int r = result[1];
        String ans = "9".repeat(q);

        if (r > 0) {
            ans += String.valueOf(r);
        }
        ans += "0".repeat(num - ans.length());

        return ans;
    }
}