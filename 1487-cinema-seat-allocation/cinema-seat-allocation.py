class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, seat in reservedSeats:
            rows.setdefault(r, set()).add(seat)

        ans = (n - len(rows)) * 2

        for seats in rows.values():
            left = all(s not in seats for s in [2, 3, 4, 5])
            right = all(s not in seats for s in [6, 7, 8, 9])
            middle = all(s not in seats for s in [4, 5, 6, 7])

            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1

        return ans