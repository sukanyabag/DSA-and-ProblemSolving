/* 
Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list!

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Constraints:
The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node

**Intuition** - The approach is to copy the next node’s value in the deleted node. 
Then, link node to next of next node. This does not delete that node but indirectly it removes that node from the linked list.

TIME - O(1)  It is a two-step process that can be obtained in constant time.
SPACE - O(1)
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        //copy the next node’s value in the node to be deleted
        node.val = node.next.val;
        //link node to next of next node
        node.next = node.next.next;
    }
}


