/*
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
*/

TURTLE RABBIT APPROACH 
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 
 TC - O(N), SC - O(1)
 Explanation - In the Turtle-Rabbit approach, we increment slow ptr by 1 and fast ptr by 2, so fast ptr 
 will travel double than that of the slow pointer. So when the fast ptr will be at the end of Linked List,
 slow ptr would have covered half of Linked List till then. So slow ptr will be pointing towards the middle node of Linked List.
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode turtle = head, rabbit = head;
        
        while(rabbit != null && rabbit.next != null){
            turtle = turtle.next;
            rabbit = rabbit.next.next;
        }
        
        return turtle;
        
    }
}
