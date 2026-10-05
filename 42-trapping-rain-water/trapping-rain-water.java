class Solution {
    public int trap(int[] height) {
        int n = height.length;

        int l = 0;
        int r = 0;

        int [] max_l = new int[n];
        int [] max_r = new int[n];

        for(int i=0; i<n; i++){
            int j = n-1-i;
            max_l[i] = l;
            max_r[j] = r;

            l = Math.max(l,height[i]);
            r = Math.max(r,height[j]);
        }

        int sum = 0;

        for(int i=0; i<n; i++){
            int gap = Math.min(max_l[i],max_r[i]);
            sum += Math.max(0, gap-height[i]);
        }


        return sum;

    }
}