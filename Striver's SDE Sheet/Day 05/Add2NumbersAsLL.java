/*
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode start = new ListNode(0);
        ListNode curr = start;
        int carry= 0;
        while(l1 != null || l2 != null || carry != 0){
            int sum = 0;
            //if l1 has not exhausted 
            if(l1!= null){
                sum += l1.val;
                l1 = l1.next;
            }
            //if l2 has not exhausted
            if(l2!= null){
                sum += l2.val;
                l2 = l2.next;
            }
            
            //add carry to sum if it exists
            sum += carry;
            
            //calculate the next carry from current sum
            carry = sum/10;
            
            //create new node with the modulo of curr sum
            // if l1.val is 6 and l2.val is 4, then it gives 10
            // 10 % 10 = 0 and that 0 is the newnode 
            // and carry is 1 which goes to next sum
            ListNode newnode = new ListNode(sum%10);
            
            //adding newnode to the resultant LL
            curr.next = newnode;
            //moving the current node to next node
            curr = newnode;
        }
        // after all possible iterations return start.next
        return start.next;
    }
}
