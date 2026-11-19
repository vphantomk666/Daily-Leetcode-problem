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
    public ListNode partition(ListNode head, int x) {
        ListNode dummy1 = new ListNode(0);
        ListNode dummy2 = new ListNode(0);
        ListNode prev = dummy1;
        ListNode curr = dummy2;
        ListNode node = head;

        while (node != null){
            if (node.val < x){
                prev.next = node;
                prev = prev.next;
            }
            else{
                curr.next = node;
                curr = curr.next;
            }
            node = node.next;
        }
        curr.next = null;
        prev.next = dummy2.next;
        return dummy1.next;
        
    }
}