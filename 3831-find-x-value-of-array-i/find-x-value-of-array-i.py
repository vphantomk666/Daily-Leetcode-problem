from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        result = [0] * k
        prevCount = [0] * k

        for i in range(n):
            currCount = [0] * k

            currElement = nums[i] % k

            currCount[currElement] += 1

            for oldRem in range(k):
                newRem = (oldRem * nums[i]) % k

                currCount[newRem] += prevCount[oldRem]

            prevCount = currCount

            for rem in range(k):
                result[rem] += prevCount[rem]

        return result