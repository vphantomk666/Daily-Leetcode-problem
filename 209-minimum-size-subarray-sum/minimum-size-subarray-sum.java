import java.util.*;

class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int left = 0;
        int curr = 0;
        int minLen = Integer.MAX_VALUE;

        for (int right = 0; right < n; right++) {
            curr += nums[right];

            while (curr >= target) {
                minLen = Math.min(minLen, right - left + 1);
                curr -= nums[left];
                left++;
            }
        }

        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}