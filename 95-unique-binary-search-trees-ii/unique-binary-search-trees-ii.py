# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        memo = {}
        def dp(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            tree = []

            if i>j:
                tree.append(None)
                return tree
            
            for root_val in range(i,j+1):
                left_trees = dp(i, root_val-1)
                right_trees = dp(root_val+1, j)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val,left, right)
                        tree.append(root)
            
            memo[(i,j)] = tree
            return tree

        return dp(1,n)