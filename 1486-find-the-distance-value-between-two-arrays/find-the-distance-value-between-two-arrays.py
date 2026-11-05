class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # cnt = 0

        # arr2.sort()

        # for i in range(len(arr1)):
        #     flag = True

        #     for j in range(len(arr2)):
        #         if abs(arr1[i] - arr2[j]) <= d:
        #             flag = False
        #             break

        #     if flag:
        #         cnt += 1

        # return cnt
                    

        cnt = 0
        arr2.sort()  
        for x in arr1: 
            idx = bisect.bisect_left(arr2, x - d)
            
            if idx == len(arr2) or arr2[idx] > x + d:
                cnt += 1

        return cnt



        
        
