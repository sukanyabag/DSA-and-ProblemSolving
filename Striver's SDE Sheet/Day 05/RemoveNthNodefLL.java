/*  
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass? SOLUTION BELOW IS DONE IN SINGLE PASS

Time Complexity: O(N)

Space Complexity: O(1)
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        //create a dummy node start
        ListNode start = new ListNode();
        //point start to head of the linked list
        start.next = head;
        //create 2 pointers and init them to start
        ListNode slow = start;
        ListNode fast = start;
        
       
        
        //now move fast pointer till n iterations
        for(int i =1; i<=n; ++i){
            fast = fast.next;
        }
        
        //next move slow and fast pointers together
        //until fast reaches null
        while(fast.next != null){
            fast = fast.next;
            slow = slow.next;
        }
        
        //cut the link
        slow.next = slow.next.next;
        
        
        return start.next;
    }
}
