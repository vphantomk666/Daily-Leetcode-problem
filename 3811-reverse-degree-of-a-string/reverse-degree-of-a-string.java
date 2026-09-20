class Solution {
    public int reverseDegree(String s) {
        int degree = 0;
        for(int i=1; i<s.length()+1; i++){
            degree += Math.abs('z' - s.charAt(i - 1)+1)*i;
        }
        return degree;
    }
}
