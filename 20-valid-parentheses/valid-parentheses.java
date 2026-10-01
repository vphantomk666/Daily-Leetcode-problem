class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put(']', '[');
        mapping.put('}', '{');

        Stack<Character> st = new Stack<>();
        for(Character ch : s.toCharArray()){

            if(!mapping.containsKey(ch)){
                st.push(ch);
            }

            else{
                if (st.isEmpty() || st.pop() != mapping.get(ch)){
                    return false;
                }
            }
        }

        return st.isEmpty();
    }
}