/*  
Problem Statement: Given the head of a linked list, rotate the list to the right by k places.

Examples:

Example 1:
Input:
	head = [1,2,3,4,5] 
	k = 2
Output:
 head = [4,5,1,2,3]
Explanation:
 We have to rotate the list to the right twice.

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
 
Time Complexity: O(length of list) + O(length of list – (length of list%k))

Reason: O(length of the list) for calculating the length of the list. O(length of the list – (length of list%k)) for breaking link.

Space Complexity: O(1)
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        //edge
        if(head == null || head.next == null || k == 0) return head;
        
        //calc length of linked list 
        ListNode temp = head;
        int length = 1;
        //until we have reached null, keep traversing
        while(temp.next != null){
            length++;
            temp = temp.next;
        }
        
        //now link the last node to the first node
        //this makes it circular
        temp.next = head;
        //when k is more than length of list,
        //then we need to rotate list by k%length times.
        k = k%length;
        //if we are rotating last k nodes, 
        //we are left with length-k nodes. So, (len-k)th node has to be set to null
        
        /* for ex-  
        1 2 3 4 5 , k=2 , so len = 5, hence 5-2= 3. So 3rd node will point to null
        after last k nodes are rotated. 
        4 5 1 2 3 -> null.
        */
        k = length-k;
        
        while(k-- > 0) temp = temp.next;
        
        //break last node link , here head will be set to temp.next, so head = 4
        head = temp.next;
        //temp.next will be set to null
        temp.next = null;
        
        return head;
        
    }
}
