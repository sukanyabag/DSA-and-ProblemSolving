/*
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Constraints:
The number of nodes in the tree is in the range [0, 2000].
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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        //init result
        List<List<Integer>> res = new LinkedList<>();
        
        //base case check
        if(root == null) 
            return res;
        
        //declare queue
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        
        //push root to queue before starting anything
        q.add(root);
        
        //set a boolean flag
        //default value of flag will be false -> which indicate left->right
        //otherwise nodes will be pushed in right -> left fashion
        boolean leftToRight = false;
        
        //traverse thro the entire size of the queue
        while(!q.isEmpty()){
            int sizeq = q.size();
             LinkedList<Integer> subList = new  LinkedList<>();
            
            //loop that traverses thro each node of binary tree
            //checks if flag is false -> appends nodes in L->R fashion. otherwise R->L
            for(int i = 0; i < sizeq; i++){
                //take it out
                TreeNode node = q.poll();
                
                //check left subtree or right subtree and push it to queue
                if(node.left != null)
                    q.add(node.left);
                
                if(node.right != null)
                    q.add(node.right);
                
                //if flag false insert it to subList from the front(L->R) -> addFirst
                //otherwise insert it to subList from the back (R->L) -> addLast
                //insert
                if(leftToRight)
                    subList.addFirst(node.val);
                else
                    subList.addLast(node.val);
            }
            
            //after for loop is executed for a particular level
            //reset flag to true 
            //append subList to res
            leftToRight = !leftToRight;
            res.add(subList);
            
        }
        
        return res;
    }
}
