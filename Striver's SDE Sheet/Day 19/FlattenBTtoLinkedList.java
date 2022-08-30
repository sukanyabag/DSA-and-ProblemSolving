/**
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)? by Morris PostOrder Traversal
**/

// REVERSE POSTORDER RECURSION
class Solution {
    TreeNode prev = null;
    public void flatten(TreeNode node) {
        //base case
        if(node == null) return;
        
        //traverse - right left root -> reverse postorder + recursion
        flatten(node.right);
        flatten(node.left);
        
        //set node's right to prev
        node.right = prev;
        //set node's left to null
        node.left = null;
        
        //update prev to last node
        prev = node;
    }
}

// ITERATIVE 
class Solution {
    public void flatten(TreeNode root) {
        //base 
         if (root == null) return;
        //init stack
        Stack<TreeNode> st = new Stack<>();
        
        //push root to stack
        st.add(root);
        
        //pick the top last element out (lifo)  and pop it out
        while(!st.isEmpty()){
            TreeNode curr = st.peek();
            st.pop();
            
            if(curr.right != null){
                st.add(curr.right);
            }
            if(curr.left != null){
                st.add(curr.left);
            }
            
            //since left is added at last, stack makes sure to pop the left first
            //so after left is popped, we set it to curr.right, and curr.left to null
            if(!st.isEmpty()){
                curr.right = st.peek();
            }
            
            curr.left = null;
            
        }
    }
}

//MORRIS POSTORDER
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
The algorithm can be described as:

At a node(say cur) if there exists a left child, we will find the rightmost node in the left subtree(say prev).
We will set prev’s right child to cur’s right child,
We will then set cur’s right child to it’s left child.
We will then move cur to the next node by assigning cur it to its right child
We will stop the execution when cur points to NULL.
 */
class Solution {
    public void flatten(TreeNode root) {
        TreeNode cur = root;
		while (cur!=null)
		{
			if(cur.left!=null)
			{
				TreeNode pre = cur.left;
				while(pre.right!=null)
				{
					pre = pre.right;
				}
				pre.right = cur.right;
				cur.right = cur.left;
				cur.left = null;
			}
			cur = cur.right;
		}
    }
}
