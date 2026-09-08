class Solution {
    public long countCommas(long n) {
        long res = 0;

        long lower = 1000;

        long commas = 1;

        while (lower<=n){
            long upper = lower*1000-1;
            if (upper > n) upper = n;

            long countcommas = upper-lower+1;
            
            res += countcommas*commas;

            lower *= 1000;
            commas ++;

        }

        return res;

    }
}