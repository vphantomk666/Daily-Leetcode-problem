class Solution {
    public int minMoves(int[] nums) {
        int total = Arrays.stream(nums).sum();
        return Arrays.stream(nums).max().getAsInt()*nums.length - total;


    }
}