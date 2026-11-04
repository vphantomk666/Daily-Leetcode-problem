class Solution {
    public int calculate(String s) {

        Stack<Integer> st = new Stack<>();

        int total = 0;
        int curr = 0;
        int sign = 1;

        for (char digit : s.toCharArray()) {

            if (Character.isDigit(digit)) {
                curr = curr * 10 + (digit - '0');
            }

            else if (digit == '+' || digit == '-') {
                total += sign * curr;
                curr = 0;

                sign = (digit == '+') ? 1 : -1;
            }

            else if (digit == '(') {
                st.push(total);
                st.push(sign);

                total = 0;
                sign = 1;
            }

            else if (digit == ')') {

                total += sign * curr;
                curr = 0;

                int sign_before = st.pop();
                int total_before = st.pop();

                total = total_before + sign_before * total;
            }
        }

        total += sign * curr;

        return total;
    }
}