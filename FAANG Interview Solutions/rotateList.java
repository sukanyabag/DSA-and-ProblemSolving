class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // edge cases -a. empty linkedlist, b. only one node, c. no of rotattions=0
        if(head==null || head.next == null || k==0){
            return head;
        }
        
        // if not te edge case, compute len of list 1st
        
        ListNode dummy = head;
        int n = 1;
        while(dummy.next != null){
             n++; // acts as a counter
            dummy = dummy.next; // acts as a pointer
        }
        
        // 2nd step - point the last node to the head
        dummy.next = head;
        k = k % n; 
        k = n-k;
        
        while(k-- > 0){
            dummy = dummy.next;
        }
        
        // again take a pointer and point it to head, which will set (n-k)th node to null
        head = dummy.next;
        dummy.next = null;
        
        return head;
        
    }
}

// time complexity - O(n), Space complexity - O(1)
