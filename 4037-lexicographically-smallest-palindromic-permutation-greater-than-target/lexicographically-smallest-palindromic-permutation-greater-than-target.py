class Solution:

    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        frequency = [0] * 26

        for ch in s:
            frequency[ord(ch) - ord('a')] += 1

        middle = ""

        for c in range(26):
            if frequency[c] % 2 == 1:
                middle = chr(ord('a') + c)


        if sum(x % 2 for x in frequency) > 1:
            return ""

        half_count = [count // 2 for count in frequency]
        k = len(s) // 2

        target_half = target[:k]

        def solve(curr, half_count, target_half, i, possible):

            if i == k:

                left_half = curr
                right_half = left_half[::-1]

                cand = left_half + middle + right_half

                if cand > target:
                    return cand

                return ""

            target_idx = ord(target_half[i]) - ord('a')

            for ch in range(26):

                if half_count[ch] == 0:
                    continue


                if not possible and ch < target_idx:
                    continue

                half_count[ch] -= 1

                curr += chr(ch + ord('a'))

                is_possible = possible or ch > target_idx

                result = solve(
                    curr,
                    half_count,
                    target_half,
                    i + 1,
                    is_possible
                )

                if result:
                    return result

                curr = curr[:-1]
                half_count[ch] += 1

            return ""

        return solve("", half_count, target_half, 0, False)