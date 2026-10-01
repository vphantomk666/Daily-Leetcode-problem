class Solution {
    public int maxProfit(int[] prices) {
        
        int min_profit = prices[0];
        int max_profit = 0;
        for(int p : prices){
            if (p < min_profit){
                min_profit = p;
            }

            int profit = p - min_profit;

            if (profit > max_profit){
                max_profit = profit;
            }

        }

        return max_profit;
    }
}