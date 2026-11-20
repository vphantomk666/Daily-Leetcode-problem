/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    long max_sum = Integer.MIN_VALUE;
    private int solve(TreeNode root){

        if (root == null){
            return 0;
        }

        int l = Math.max(0, solve(root.left));
        int r = Math.max(0, solve(root.right));

        int last_good = l+r+root.val;

        max_sum = Math.max(max_sum, last_good);

        return Math.max(l,r) + root.val;
    }
    public int maxPathSum(TreeNode root) {

        solve(root);
        return (int)max_sum;
    }
}