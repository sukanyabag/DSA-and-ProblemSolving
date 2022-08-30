/**
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and 
postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
 
Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if(inorder == null || postorder == null || inorder.length != postorder.length) return null;
        
        HashMap<Integer,Integer> mp = new HashMap<>();
        
        for(int i= 0; i < inorder.length; i++){
            mp.put(inorder[i], i);
        }
        //vvimp
        return helper(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1, mp);
    }
    
    private TreeNode helper(int[] inorder, int is, int ie, int[] postorder, int ps, int pe, HashMap<Integer,Integer> mp ){
        
        //boundary check
        if(ps > pe || is > ie) return null;
        
        TreeNode root = new TreeNode(postorder[pe]);
        
        //vvimp
        int getRootIdx = mp.get(postorder[pe]);
        int numsAtLeft = getRootIdx - is;
        
        //build build build
        /*    is               ie
        in = [40 20  50 10 60  30]
              0   1  2  3   4   5
             |---L---|     |--R--|
              ps              pe
        po = [40 50 20 60  30 10]
              0   1  2  3   4  5
             |---L---|  |-R-|
        
        getRootIdx = 3
        numsAtLeft = 3 - is = 3 - 0 = 3
        so we can see that from is = 0 to getRootIdx - 1 = 2, we have our left subtree
        and, that in postorder is exactly from ps = 0 to ps(0) + numsAtLeft(3) - 1 = 2 (0 -> 2)
        
        and from getRootIdx + 1 = 3 + 1 = 4 to ie = 5, we have our right subtree. and that
        in postorder array is exactly from ps(0) + numsAtLeft(3) = 3 to pe-1 = 5 - 1 = 4
        */
        root.left = helper(inorder,is,getRootIdx-1,postorder, ps, ps + numsAtLeft - 1, mp);
        root.right = helper(inorder, getRootIdx + 1, ie, postorder, ps + numsAtLeft, pe-1, mp);
        
        return root;
        
    }
}
