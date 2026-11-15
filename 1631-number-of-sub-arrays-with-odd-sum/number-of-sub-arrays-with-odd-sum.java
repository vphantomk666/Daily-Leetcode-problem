class Solution {
    public int numOfSubarrays(int[] arr) {
        final int MOD = 1_000_000_007;

        int n = arr.length;
        int perfix = 0;
        int even = 1;
        int odd = 0;
        long ans = 0;

        for(int num: arr){
            perfix += num;

            if ((perfix & 1) == 1){
                ans += even;
                odd ++;
            }
            else{
                ans += odd;
                even++;
            }

            ans %= MOD;
        }

        return (int)ans;
    }
}