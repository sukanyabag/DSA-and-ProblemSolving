/*
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q 
as descendants (where we allow a node to be a descendant of itself).”

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || root == p || root == q) return root;
        
        //traverse the left and right subtrees to search for p and q
        TreeNode left  = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        //if one is null, return the other -> RETURN THE NON NULL NODE
        if(left == null) 
            return right;
        
        if(right == null)
            return left;
        
        //if right and left are both NON-NULL, means p and q nodes are found
        //so return its root - which will be p and q's lowest comm ancestor
        else
            return root;
        
    }
}
