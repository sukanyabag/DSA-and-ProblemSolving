/*
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
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
    //init diameter
    int dmeter = 0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        //// This will find the max depth going through each node,
        // and update the global maximum to the class member 'dmeter'
        findHeight(root);
        
        // Return the global maximum 'dmeter'
        return dmeter;
    }
    
    private int findHeight(TreeNode root){
        // Height of 'nothing' is 0
        if(root == null) return 0;
        
         // Find height of left and right subTrees (check problem height/depth of a binary tree)
        int leftHeight = findHeight(root.left);
        int rightHeight = findHeight(root.right);
        
        // New dmeter is either already reached,
        // or is acheived using current node as the root
        //max value is picked for updating dmeter
        dmeter = Math.max(dmeter, leftHeight+rightHeight);
        
        // Return height of tree calculated at this node
        return Math.max(leftHeight, rightHeight) + 1;
    }
}
