/** 
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a descendant of node.

Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Constraints:
The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
**/
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
    public TreeNode pruneTree(TreeNode root) {
        if(!containsOne(root))  root = null;
        containsOne(root);
        return root;
        
    }
    public boolean containsOne(TreeNode node){
        if(node == null) return false;
        boolean left_contains = containsOne(node.left);
        boolean right_contains = containsOne(node.right);
        if(!left_contains){
            node.left = null;
        }
        if(!right_contains){
            node.right = null;
        }
        return node.val == 1 || left_contains || right_contains;
    }
}
