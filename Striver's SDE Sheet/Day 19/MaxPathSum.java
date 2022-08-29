/*
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
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
 
Initialize a maxi variable to store our final answer.

Do a simple tree traversal. At each node, find  recursively its leftMaxPath and its rightMaxPath.

Calculate the maxPath through the node as val + (leftMaxPath + rightMaxPath) and update maxi accordingly.

Return the maxPath when node is not the curving point as val + max(leftMaxPath, rightMaxPath).
 */
class Solution {
    public int maxPathSum(TreeNode root) {
        int[] maxVal = new int[1];
        maxVal[0] = Integer.MIN_VALUE;
        maxPathDown(root, maxVal);  
        return maxVal[0];
    }
    
    private int maxPathDown(TreeNode node, int maxVal[]){
        if(node == null) return 0;
        
        int left = Math.max(0, maxPathDown(node.left, maxVal));
        int right = Math.max(0, maxPathDown(node.right, maxVal));
        
        maxVal[0] =  Math.max(maxVal[0], (left+right+node.val));
        
        return Math.max(left,right) + node.val;
        
    }
    
}
