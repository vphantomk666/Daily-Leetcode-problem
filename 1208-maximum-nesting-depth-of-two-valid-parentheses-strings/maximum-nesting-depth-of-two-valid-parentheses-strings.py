class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        result = []

        for i in range(n):
            result.append((i^ord(seq[i])) & 1)
        
        return result