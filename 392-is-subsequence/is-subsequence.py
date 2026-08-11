class Solution:
    def LCS(self,a,b,i,j):
        if i==0 or j==0:
            return 0
        if self.t[i][j] != -1:
            return self.t[i][j]
        
        if a[i-1]==b[j-1]:
            self.t[i][j] = 1+self.LCS(a,b,i-1,j-1)
        else:
            self.t[i][j] = max(self.LCS(a,b,i-1,j),self.LCS(a,b,i,j-1))

        return self.t[i][j]
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        self.t = [[-1]*(n+1) for _ in range(m+1)]

        for i in range(m):
            self.t[i][0] = 0
        for j in range(n):
            self.t[0][j] = 0
            
        return self.LCS(s,t,m,n) == m
