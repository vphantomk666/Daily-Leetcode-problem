class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o = 0
        c = 0

        for ch in s:
            if ch == '(':
                o += 1
            elif ch == ')' and o > 0:
                o -= 1 
            else:
                c += 1
        
        return  o+c





