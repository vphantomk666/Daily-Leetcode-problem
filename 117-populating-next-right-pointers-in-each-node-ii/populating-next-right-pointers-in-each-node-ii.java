/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        Node node  = root;

        while (node != null){
            Node dummy = new Node(0);
            Node curr = dummy;

            while(node != null){
                if (node.left != null){
                    curr.next = node.left;
                    curr = curr.next;
                }
                if (node.right != null){
                    curr.next = node.right;
                    curr = curr.next;
                }
                node = node.next;
            }

            node = dummy.next;
        }

        return root;
    }
}