/*
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 2000].
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
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        List<List<Integer>> levOrder = new LinkedList<List<Integer>>();
        //base case
        if(root == null) return levOrder;
        //add 1st level -> always the root
        q.offer(root);
        
        //iter until queue is not empty
        while(!q.isEmpty()){
            int size = q.size();
            //level - sublist of a particular level
            List<Integer> level = new LinkedList<Integer>();
            //loop until queue is exhausted
            for(int i = 0; i < size; i++){
                //if any element at queue's front has a left child/right child, add them to queue
                if(q.peek().left != null) q.offer(q.peek().left);
                if(q.peek().right != null) q.offer(q.peek().right);
                //add the level to the level sublist
                level.add(q.poll().val);
            }
            // add every level sub-list to the resultant list levOrder, which stores the entire level order traversal
             levOrder levOrder.add(level);
        }
        return levOrder;
    }
}
