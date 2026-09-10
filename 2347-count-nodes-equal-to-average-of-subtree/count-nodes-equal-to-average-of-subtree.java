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
    int count = 0;

    private int[] dfs(TreeNode node){
        if (node == null){
            return new int[] {0,0};
        }

        int[] left = dfs(node.left);
        int[] right = dfs(node.right);

        int root_sum = node.val + left[0] + right[0];
        int root_cnt = 1 + left[1] + right[1];

        int res = root_sum / root_cnt;

        if (res == node.val){
            count ++;
        }

        return new int[] {root_sum, root_cnt};
    }
    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return count;
    }
}