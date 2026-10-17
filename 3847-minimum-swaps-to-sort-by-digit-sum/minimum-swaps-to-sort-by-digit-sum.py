from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        n = len(nums)

        res = []
        for i, num in enumerate(nums):
            res.append((get_digit_sum(num), num, i))

        res.sort()

        target = [0] * n
        for sorted_idx, (_, _, original_idx) in enumerate(res):
            target[original_idx] = sorted_idx

        visited = [False] * n
        cnt = 0

        for i in range(n):
            if visited[i] or target[i] == i:
                continue

            cycle_len = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target[j]
                cycle_len += 1

            cnt += cycle_len - 1

        return cnt