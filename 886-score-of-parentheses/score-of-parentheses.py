class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        st = []
        src = 0

        for i in range(n):
            if s[i] == '(':
                st.append(src)
                src = 0
            else:
                if s[i-1] == '(':
                    src = st[-1] + 1
                else:
                    src = st[-1] + 2*src
                st.pop()
            
        return src
            
            