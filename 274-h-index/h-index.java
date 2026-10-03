class Solution {
    public int hIndex(int[] c) {
        int n = c.length;

        int[] dp = new int[n+1];

        for(int num : c){
            if (num >= n){
                dp[n]++;}
            else{
                dp[num]++;
            }
        }
        

        int total = 0;

        for(int i = n; i>0; i--){
            total += dp[i];

            if (total >= i){
                return i;
            }
        }

        return 0;
        
    }
}
