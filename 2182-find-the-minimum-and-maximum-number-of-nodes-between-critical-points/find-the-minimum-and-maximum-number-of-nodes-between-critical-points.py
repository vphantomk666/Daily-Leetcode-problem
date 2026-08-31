# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        fcp = float('inf')   # first critical point
        pcp = -1             # previous critical point
        minDist = float('inf')

        prev = head
        curr = head.next
        i = 1

        while curr and curr.next:
            # local minima OR local maxima
            if (prev.val > curr.val < curr.next.val) or \
            (prev.val < curr.val > curr.next.val):

                if fcp == float('inf'):
                    fcp = i
                else:
                    minDist = min(minDist, i - pcp)

                pcp = i

            prev = curr
            curr = curr.next
            i += 1

        if fcp == float('inf') or fcp == pcp:
            return [-1, -1]

        return [minDist, pcp - fcp]