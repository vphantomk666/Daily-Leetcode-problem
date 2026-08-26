class Solution {
    public String shortestBeautifulSubstring(String s, int k) {

        String res = "";
        int one = 0;
        int l = 0;

        for (int r = 0; r < s.length(); r++) {

            if (s.charAt(r) == '1') {
                one++;
            }

            while (one > k) {
                if (s.charAt(l) == '1') {
                    one--;
                }
                l++;
            }

            if (one == k) {

                while (s.charAt(l) == '0') {
                    l++;
                }

                String curr = s.substring(l, r + 1);

                if (res.isEmpty() ||
                    curr.length() < res.length() ||
                    (curr.length() == res.length() &&
                     curr.compareTo(res) < 0)) {

                    res = curr;
                }
            }
        }

        return res;
    }
}