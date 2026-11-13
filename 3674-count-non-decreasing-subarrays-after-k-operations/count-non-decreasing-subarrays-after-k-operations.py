
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dq = deque()

        cost = 0
        ans = 0

        j = n - 1

        for i in range(n - 1, -1, -1):

            num = nums[i]
            count = 1

            # Merge smaller groups into the current group
            while dq and dq[-1][0] < num:

                nextNum, nextCount = dq.pop()

                cost += (num - nextNum) * nextCount

                count += nextCount

            dq.append((num, count))

            # Maintain cost <= k
            while cost > k:

                rightmostNum, rightmostCount = dq.popleft()

                cost -= rightmostNum - nums[j]

                j -= 1

                if rightmostCount > 1:
                    dq.appendleft((rightmostNum, rightmostCount - 1))

            # Count valid subarrays ending at j
            ans += j - i + 1

        return ans
