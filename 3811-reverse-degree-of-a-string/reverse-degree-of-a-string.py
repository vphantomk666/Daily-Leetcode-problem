class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(abs(ord(st) - (ord('z')+1)) * i for i, st in enumerate(s, start=1)) 
