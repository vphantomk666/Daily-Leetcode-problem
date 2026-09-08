class Solution {
    public long countCommas(long n) {
        long res = 0;

        long Start = 1000;


        while (Start<=n){
            res += (n-Start)+1;

            Start *= 1000;
        }
        return res;

    }
}