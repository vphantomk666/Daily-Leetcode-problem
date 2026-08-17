class Solution:
    def stoneGameV(self, s: List[int]) -> int:
        n = len(s)

        score_sums = list(accumulate(s, initial=0))

        @cache
        def dp(i, j):

            if i == j:
                return 0

            max_score = 0

            for k in range(i, j):

                left = score_sums[k + 1] - score_sums[i]
                right = score_sums[j + 1] - score_sums[k + 1]

                if left < right:

                    if max_score >= 2 * left:
                        continue

                    max_score = max(
                        max_score,
                        left + dp(i, k)
                    )
                                                                         
                elif left > right:
                    if max_score >= 2 * right:
                        break

                    max_score = max(
                        max_score,
                        right + dp(k + 1, j)
                    )

                else:

                    max_score = max(
                        max_score,
                        left + dp(i, k),
                        right + dp(k + 1, j)
                    )

            return max_score

        return dp(0, n - 1)