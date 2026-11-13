class Solution {
    public int climbStairs(int n) {
        if (n==1 || n==2){
            return n;
        }

        int two_back = 1;
        int one_back = 2;

        for(int i=2; i<n; i++){
            int temp = two_back+one_back;
            two_back = one_back;
            one_back = temp;
        }


        return one_back;
    }
}