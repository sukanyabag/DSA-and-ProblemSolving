/*
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
*/

//RECURSIVE
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if(root == null) {
            return true;
    }
        return isSymmetric(root.left, root.right);
     
    }
    public boolean isSymmetric(TreeNode left, TreeNode right){
        if(left == null || right == null){
            return left == right;
        }
        
        if(left.val != right.val){
            return false;
        }
        
        return isSymmetric(left.left, right.right) && isSymmetric(left.right,right.left);
        
    }
}

//ITERATIVE
public boolean isSymmetric(TreeNode root) {
        if(root == null)
            return true;
        Queue<TreeNode> q = new LinkedList();
       
        q.add(root.left);
        q.add(root.right);
        while(!q.isEmpty()){
            TreeNode left = q.poll();
            TreeNode right = q.poll();
            if(left == null && right == null)
                continue;
            if(left == null || right == null ||left.val != right.val )
                return false;
            q.add(left.left);
            q.add(right.right);
            q.add(left.right);
            q.add(right.left);
            
        }
        return true;
            
