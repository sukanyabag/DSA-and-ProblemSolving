/*
Problem Description
Given a Binary Tree A containing N nodes.
You need to find the path from Root to a given node B.
NOTE:
No two nodes in the tree have same data values.
You can assume that B is present in the tree A and a path always exists.

Problem Constraints
 1 <= N <= 105 
 1 <= Data Values of Each Node <= N
 1 <= B <= N
 
Input Format
First Argument represents pointer to the root of binary tree A.
Second Argument is an integer B denoting the node number.

Output Format
Return an one-dimensional array denoting the path from Root to the node B in order.
*/

/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) {
 *      val = x;
 *      left=null;
 *      right=null;
 *     }
 * }
 */
public class Solution {
    public ArrayList<Integer> solve(TreeNode A, int B) {
       ArrayList<Integer> arr = new ArrayList<Integer>();
        if(A == null) return arr;
        getPath(A, arr, B);
        return arr;
    }
    
    private boolean getPath(TreeNode root, ArrayList<Integer> arr, int target){
        if(root == null) return false;
        
        arr.add(root.val);
        //if already root is our target node
        if(root.val == target){
            return true;
        }
    
        
        if(getPath(root.left,arr,target) || getPath(root.right, arr, target)){
            return true;
        }
        
        //remove last entry in case no path to target is found
        arr.remove(arr.size() - 1);
        return false;
    }
}
