/*  
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        //base cases
        if(list1 == null) return list2;
        if(list2 == null) return list1;
        
       //treat list1 and list2 as two pointers
        //then compare first nodes of both and find smaller among the two
        //assign list1 to the small value if list1's value is greater than list2's
        //so swap list1 and list2 if list1's val > list2's val
        if(list1.val > list2.val){
            ListNode temp = list1;
            list1 = list2;
            list2 = temp;
        }
        
      //now init a res listnode whichpoints to list1
        ListNode res = list1;
       //iterate through both lists list1 and list2, till list1's value is <= list2's value
        while(list1 != null && list2 != null){
           //tmp keeps track of last node visited in the sorted lists list1 and list2
            ListNode tmp = null;
            while(list1 != null && list1.val <= list2.val){
                tmp = list1;
                list1 = list1.next;
            }
            
            //iteration ends when list1's value is greater than list2's value
            //so now we link the node pointed by tmp to the node pointed by list2 to break bond/link 
            tmp.next = list2;
            
            //then swap list1 and list2 so that node with lesser value is set to list1 pointer
            ListNode temp = list1;
            list1 = list2;
            list2 = temp;
            
        }
        
        return res;
        
    }
}
