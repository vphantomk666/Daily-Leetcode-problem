class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();

        int len = 0;
        StringBuilder curr = new StringBuilder();
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);

            int idx = curr.indexOf(String.valueOf(ch));

            if (idx != -1) {
                len = Math.max(len, cnt);

                curr.delete(0, idx + 1);
                cnt = curr.length();
            }

            curr.append(ch);
            cnt++;

            len = Math.max(len, cnt);
        }

        return len;
    }
}