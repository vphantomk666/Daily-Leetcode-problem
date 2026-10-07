class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []
        n = len(s)
        maxlen = 0
        def solve(i, curr, cnt):
            nonlocal maxlen

            if cnt < 0:
                return

            if i == n:
                if cnt == 0:
                    if len(curr) > maxlen:
                        maxlen = len(curr)
                        res.clear()
                        res.append(curr)

                    elif len(curr) == maxlen:
                        if curr not in res:
                            res.append(curr)

                return

            if s[i] not in "()":
                solve(i + 1, curr + s[i], cnt)
                return


            if s[i] == '(':
                solve(i + 1, curr + s[i], cnt + 1)
            else:
                solve(i + 1, curr + s[i], cnt - 1)

            solve(i + 1, curr, cnt)

        solve(0, "", 0)

        return res

        