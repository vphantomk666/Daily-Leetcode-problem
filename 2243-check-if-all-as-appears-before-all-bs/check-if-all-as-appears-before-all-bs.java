class Solution {
    public boolean checkString(String s) {
        char[] arr = s.toCharArray();

        Arrays.sort(arr);

        return s.equals(new String(arr));   
    }
}