class Solution {
    public long[] resultArray(int[] nums, int k) {
        int n = nums.length;

        long[] result = new long[k];
        long[] prevCount = new long[k];

        for (int i = 0; i < n; i++) {

            long[] currCount = new long[k];

            int currElement = nums[i] % k;

            currCount[currElement]++;

            for (int oldRem = 0; oldRem < k; oldRem++) {

                int newRem = (int)(((long) oldRem * nums[i]) % k);

                currCount[newRem] += prevCount[oldRem];
            }

            prevCount = currCount;

            for (int rem = 0; rem < k; rem++) {
                result[rem] += prevCount[rem];
            }
        }

        return result;
    }
}