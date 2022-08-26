/*
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:
Input: root = [1]
Output: ["1"]
 
Constraints:
The number of nodes in the tree is in the range [1, 100].
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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        
        helper(res,root,sb);
        return res;
    }
    
    private static void helper(List<String> res, TreeNode root, StringBuilder sb){
        //base case 
        if(root == null) return;
        
        //length of sb
        int len = sb.length();
        
        //preord traversal - root.val, root.left, root.right
        sb.append(root.val);
        
        //edge case-  check if root's left and right child is null
        //if yes,we add the sb to the res by comverting it to str
        if(root.left == null && root.right == null){
            res.add(sb.toString());
        }
        
        //otherwise, traverse and append left and then right child
        else{
            sb.append("->");
            //call recursion on left and right child resp
            helper(res, root.left, sb);
            helper(res,root.right, sb);
        }
        
        //update sb to new length
        sb.setLength(len);
    }
}
