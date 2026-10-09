class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)

        cnt = 0
        res = 0
        i = 0

        while i<n:
            if s[i] == '(':
                cnt += 1
                i += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    res += 1
                
                if i+1 < n and s[i+1] == ')':
                    i += 2
                else:
                    res += 1
                    i += 1
            
        return res + 2*cnt