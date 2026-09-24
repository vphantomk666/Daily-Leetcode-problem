class Solution {

    private int digitsum(int n){
        int total = 0;
        while (n > 0){
            int digit = n % 10;
            total = total+digit;
            n /= 10;
        }
        return total;
    }
    public int smallestIndex(int[] nums) {
        int n = nums.length;
        int index = Integer.MAX_VALUE;
        for(int i = 0; i < n; i++){
            if (i == digitsum(nums[i])){
                index = Math.min(index, i);
            }
        }

        return index == Integer.MAX_VALUE? -1 : index;
    }
}