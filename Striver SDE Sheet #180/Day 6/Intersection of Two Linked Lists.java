/*  
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Note that the linked lists must retain their original structure after the function returns.
Custom Judge:
The inputs to the judge are given as follows (your program is not given these inputs):
intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 
Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 
Time Complexity: O(2*max(length of list1,length of list2))
Reason: Uses the same concept of difference of lengths of two lists.
Space Complexity: O(1)
Reason: No extra data structure is used
 */

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        //edge case check
        if(headA == null || headB == null) return null;
        
        ListNode dummy1 = headA;
        ListNode dummy2 = headB;
        
        //loop as long as dummy1 is not equal to dummy2
        while(dummy1 != dummy2){
            /* the following to steps are done to 
            ensure dummy1 and dummy2 are perfectly inclined with 
            each other so that they can collide 
            when intersection node is reached */
            //if dummy1 reaches null set it to headB, else keep moving it by 1 step
            //if dummy2 reaches null set it to headA, else keep moving it by 1 step
            dummy1 = (dummy1 == null) ? headB : dummy1.next;
            dummy2 = (dummy2 == null) ? headA : dummy2.next;
        }
        
        return dummy1;
    }
}
