class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        curr = ""
        def solve(curr, n, open, close):
            if len(curr) == 2*n:
                result.append(curr)
                return

            if open < n:
                solve(curr + "(", n, open + 1, close)
            if close < open:
                solve(curr + ")", n, open, close + 1) 
        

        solve(curr, n, 0, 0)

        return result




