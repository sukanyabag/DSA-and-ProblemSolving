/* 
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
Input: head = [1,2,2,1]
Output: true

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?
*/
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
    public boolean isPalindrome(ListNode head) {
        //edge case
        if(head==null||head.next==null) return true;
        
        ListNode slow = head;
        ListNode fast = head;
        
        //middle elm
        while(fast.next!=null&&fast.next.next!=null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        slow.next = reverse(slow.next);
        slow = slow.next;
        ListNode dummy = head;
        
        while(slow!=null){
            if(dummy.val != slow.val) return false; //not a pal
            dummy = dummy.next;
            slow = slow.next;
        }
        
        return true;
        
    }
    
    public static ListNode reverse(ListNode head){
        ListNode dummy = null;
        while(head!=null){
            ListNode next = head.next;
            head.next = dummy;
            dummy = head;
            head = next;
        }
        return dummy;
    }
}
