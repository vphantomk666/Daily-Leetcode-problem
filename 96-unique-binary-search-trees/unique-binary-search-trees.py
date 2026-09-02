class Solution:
    def numTrees(self, n: int) -> int:
        trees = [1]*(n+1)

        for node in range(2,n+1):
            total = 0
            for root in range(1,node+1):
                total += trees[root-1]*trees[node-root]
            trees[node] = total
        
        return trees[n]