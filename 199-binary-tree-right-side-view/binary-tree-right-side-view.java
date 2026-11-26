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
    public List<Integer> rightSideView(TreeNode root) {

        List<Integer> res = new ArrayList<>();

        if (root == null) {
            return res;
        }

        Queue<TreeNode> que = new LinkedList<>();
        que.offer(root);

        while (!que.isEmpty()) {

            int n = que.size();
            int last = 0;

            for (int i = 0; i < n; i++) {

                TreeNode node = que.poll();

                last = node.val;

                if (node.left != null) {
                    que.offer(node.left);
                }

                if (node.right != null) {
                    que.offer(node.right);
                }
            }

            res.add(last);
        }

        return res;
    }
}

