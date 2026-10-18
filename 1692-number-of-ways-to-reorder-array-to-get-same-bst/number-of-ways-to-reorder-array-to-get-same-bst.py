
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        pt = [[1] * (i + 1) for i in range(n + 1)]

        for i in range(2, n + 1):
            for j in range(1, i):
                pt[i][j] = (pt[i - 1][j - 1] + pt[i - 1][j]) % mod

        def solve(arr):
            size = len(arr)

            if size < 3:
                return 1

            root = arr[0]
            left = []
            right = []

            for num in arr[1:]:
                if num < root:
                    left.append(num)
                else:
                    right.append(num)

            x = solve(left)
            y = solve(right)

            z = pt[size - 1][len(left)]

            return (x * y % mod) * z % mod

        return (solve(nums) - 1) % mod
