class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = []

        for l in range(len(s)):
            one = 0

            for r in range(l,len(s)):

                if s[r] == "1":
                    one += 1
                
                if one == k:
                    res.append(s[l:r+1])
                    break

                if one > k :
                    break

        if not res:
            return ""

        min_len = min(map(len, res))

        return min(x for x in res if len(x) == min_len)

                
        