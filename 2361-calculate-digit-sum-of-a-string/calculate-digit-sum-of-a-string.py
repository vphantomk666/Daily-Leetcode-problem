
class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            result = []

            for i in range(0, len(s), k):
                total = 0

                for ch in s[i:i+k]:
                    total += int(ch)

                result.append(str(total))

            s = "".join(result)

        return s
