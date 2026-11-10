/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {

        if (head == null || head.next == null) {
            return head;
        }

        ListNode curr = head;

        int l = 1;

        while (curr.next != null){
            l += 1;
            curr = curr.next;
        }

        k = k%l;

        if (k == 0){
            return head;
        }

        curr.next = head;

        int step = l-k;
        curr = head;

        for( int i=0; i<step-1; i++){
            curr = curr.next;
        }

        ListNode new_head = curr.next;
        curr.next = null;


        return new_head;



       
    }
}