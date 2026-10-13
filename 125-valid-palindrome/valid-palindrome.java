class Solution {
    public boolean isPalindrome(String s) {
        String res = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");

        int i = 0, j = res.length()-1;

        while (i < j){

            if (res.charAt(i) != res.charAt(j)){
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
}