class Solution {
    public String simplifyPath(String path) {
        Stack<String> st = new Stack<>();
        String[] comp = path.split("/");

        for(String cp : comp){
            if(cp.equals("") || cp.equals(".")){
                continue;
            }

            if (cp.equals("..")){
                if(!st.isEmpty()){
                    st.pop();
                }
            }
            else{
                    st.push(cp);
            }
            
        }

        StringBuilder sb = new StringBuilder();

        while(!st.isEmpty()){
            sb.insert(0,"/"+st.pop());
        }

        return sb.length() == 0 ? "/" :sb.toString();
    }
}