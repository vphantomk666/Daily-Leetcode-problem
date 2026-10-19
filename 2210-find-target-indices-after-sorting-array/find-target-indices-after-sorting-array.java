class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        int idx = 0;
        int cnt = 0;

        List<Integer> res = new ArrayList<>();

        for(int i=0; i<nums.length; i++){
            if (nums[i] < target){
                idx++;
            }
            else if (nums[i] == target){
                cnt++;
            }
        }

        for( int i=0; i<cnt; i++){
            res.add(i+idx);
        }

        return res;
    }
}