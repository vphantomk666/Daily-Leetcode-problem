class Solution {
    public boolean stoneGameIX(int[] stones) {
        int cnt0 = 0; 
        int cnt1 = 0;
        int cnt2 = 0;

        for(int s : stones){
            if (s%3 == 0){
                cnt0 += 1;
            }
            else if (s%3 == 1){
                cnt1 += 1;
            }
            else{
                cnt2 += 1;
            }
        }
        
        if(cnt0%2 == 0){
            return cnt1 > 0 && cnt2 > 0;
        }

        return Math.abs(cnt1-cnt2) > 2;
        
    }
}