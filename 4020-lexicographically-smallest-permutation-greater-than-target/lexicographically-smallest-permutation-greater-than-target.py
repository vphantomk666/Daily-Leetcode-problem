class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        char = [0] * 26
        curr = ""

        for ch in s:
            char[ord(ch) - ord('a')] += 1

        def solve(curr, char, target, i, possible):
            if i == len(target):
                if possible:
                    return curr
                return ""

            for ch in range(26):
                if char[ch] == 0:
                    continue

                if not possible and ch < ord(target[i]) - ord('a'):
                    continue

                curr += chr(ch + ord('a'))
                char[ch] -= 1

                ispossible = possible or ch > ord(target[i]) - ord('a')

                result = solve(curr, char, target, i + 1, ispossible)

                if result:
                    return result

                curr = curr[:-1]
                char[ch] += 1

            return ""

        return solve(curr, char, target, 0, False)