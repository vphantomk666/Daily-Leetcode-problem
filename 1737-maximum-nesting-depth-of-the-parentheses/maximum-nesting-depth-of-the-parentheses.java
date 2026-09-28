class Solution {
    public int maxDepth(String s) {
        int cnt = 0;
        int depth = 0;

        for(char str : s.toCharArray()){
            if (str == '('){
                cnt++;
                depth = Math.max(depth, cnt);
            }
            else if (str == ')'){
                cnt--;
            }
        }

        return depth;
    }
}