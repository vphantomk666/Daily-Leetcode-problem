class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        depth = 0
        for val in s:

            if val == '(':
                cnt += 1
                depth = max(depth, cnt)

            elif val == ')':
                cnt -= 1
            
        return depth

        


