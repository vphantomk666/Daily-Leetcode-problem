class Solution:

    def build_palindrome(self, half: str, middle: str) -> str:
        return half + middle + half[::-1]

    def smallest_greater_or_equal(self, original_count, target_half: str) -> str:
        count = original_count[:]
        k = len(target_half)
        matched = 0

        while matched < k and count[ord(target_half[matched]) - ord('a')] > 0:
            count[ord(target_half[matched]) - ord('a')] -= 1
            matched += 1

        if matched == k:
            return target_half

        for pos in range(matched, -1, -1):
            if pos < matched:
                count[ord(target_half[pos]) - ord('a')] += 1

            current = ord(target_half[pos]) - ord('a')

            for c in range(current + 1, 26):
                if count[c] == 0:
                    continue

                result = target_half[:pos] + chr(ord('a') + c)
                count[c] -= 1

                for ch in range(26):
                    result += chr(ord('a') + ch) * count[ch]

                return result

        return ""

    def next_permutation(self, chars) -> bool:
        pivot = len(chars) - 2

        while pivot >= 0 and chars[pivot] >= chars[pivot + 1]:
            pivot -= 1

        if pivot < 0:
            return False

        swap_pos = len(chars) - 1

        while chars[swap_pos] <= chars[pivot]:
            swap_pos -= 1

        chars[pivot], chars[swap_pos] = chars[swap_pos], chars[pivot]

        chars[pivot + 1:] = reversed(chars[pivot + 1:])

        return True

    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        frequency = [0] * 26

        for ch in s:
            frequency[ord(ch) - ord('a')] += 1

        middle = ""
        odd_count = 0

        for c in range(26):
            if frequency[c] % 2 == 1:
                odd_count += 1
                middle = chr(ord('a') + c)

        if odd_count > 1:
            return ""

        half_count = [count // 2 for count in frequency]
        k = len(s) // 2
        target_half = target[:k]

        half = self.smallest_greater_or_equal(half_count, target_half)

        if not half and k > 0:
            return ""

        candidate = self.build_palindrome(half, middle)

        if candidate > target:
            return candidate

        chars = list(half)

        if not self.next_permutation(chars):
            return ""

        return self.build_palindrome("".join(chars), middle)

# advance logic
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n, cnt = len(s), Counter(s)
        odds = [c for c, v in cnt.items() if v % 2]
        if len(odds) > n % 2:
            return ""

        mid, h = (odds[0] if odds else ""), n // 2
        pool = Counter({c: v // 2 for c, v in cnt.items()})
        build = lambda half: half + mid + half[::-1]

        stop = 0                                     # longest prefix of target[:h] the pool can match
        while stop < h and pool[target[stop]]:
            pool[target[stop]] -= 1
            stop += 1

        if stop == h and (p := build(target[:h])) > target:
            return p                                 # half forced -> exactly one candidate

        for i in range(stop, -1, -1):                # walk back to the last raisable position
            if i < h and (c := min((x for x in pool if x > target[i] and pool[x]), default="")):
                pool[c] -= 1
                return build(target[:i] + c + "".join(c * pool[c] for c in sorted(pool)))
            if i:
                pool[target[i - 1]] += 1             # un-consume, restoring the pool for i-1

        return ""
