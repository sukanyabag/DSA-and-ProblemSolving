/*
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
*/

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
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        //if returns -1 -> not balanced BT
        //otherwise balanced BT
        return maxDepth(root) != -1;
    }
    
    private int maxDepth(TreeNode root){
        //boundary check
        if(root == null) return 0;
        
        //calc heights/depths of left and right subtrees
        //with simple dfs recursive calls
        int leftHeight = maxDepth(root.left);
        int rightHeight = maxDepth(root.right);
        
        //if left/right subtree is unbalanced
        //i.e. the hight difference larger than 1,
        //the corresponding value will be -1
        if(leftHeight == -1) return -1;
        if(rightHeight == -1) return -1;
        
        //if height-difference bw left and right subtree > 1 -> not balanced
        if((Math.abs(leftHeight - rightHeight)) > 1){
            return -1;
        }
        //return balanced height -> this will return either 0 or 1 -> balanced
        return Math.max(leftHeight,rightHeight)+1;
    }
}
