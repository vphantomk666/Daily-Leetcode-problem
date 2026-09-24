class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        def digit(n):
            total = 0

            while n > 0:
                d = n % 10
                total += d
                n //= 10

            return total

        index = float('inf')

        for i, num in enumerate(nums):
            if i == digit(num):
                index = min(index, i)

        return -1 if index == float('inf') else index