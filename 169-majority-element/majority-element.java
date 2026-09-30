class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> freq = new HashMap<>();


        for(int num: nums){
            freq.put(num, freq.getOrDefault(num, 0)+1);
        }


        int maxFreq = 0;
        int ans = 0;

        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            if (entry.getValue() > maxFreq) {
                maxFreq = entry.getValue();
                ans = entry.getKey();
            }
        } 

        return ans;
    }
}
