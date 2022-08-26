/*
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
It is guaranteed that the answer will in the range of a 32-bit signed integer.

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Constraints:
The number of nodes in the tree is in the range [1, 3000].
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
class Pair{
    TreeNode node;
    int idx;
    Pair(TreeNode node, int idx){
        this.node = node;
        this.idx = idx;
    }
}
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        //base case
        if(root == null) return 0;
        //init answer
        int res = 0;
        //init queue obj with pair user def datatype to store (node,idx)
        Queue<Pair> q = new LinkedList<>();
        q.offer(new Pair(root,0));
        
        //iter till queue is not empty
        while(!q.isEmpty()){
            int size = q.size();
            int minIdx = q.peek().idx;
            int first = 0;
            int last = 0;
            
            for(int i = 0; i < size; i++){
                //to avoid ovf( it can happen in a tree that we overshoot the bound of an integer)
                //Therefore, subtract any i idx with minIdx of that level, so for idx = 1, we just reset its id to 1-1 = 0, for 2, 2 - 1 = 1 and so on...
                int cur_id = q.peek().idx-minIdx;
                TreeNode node = q.peek().node;
                q.poll();
                
                //if i is at beginning, set first idx(min) to cur_id
                if(i == 0) first = cur_id;
                //if i is at end, set last idx(max) to cur_id
                if(i == size - 1) last = cur_id;
                
                //tag upcoming left and right nodes' indexes with cur_id*2+1, cur_id*2+2 resp
                //So, for cur_id 0...
                //left child will have idx id 0*2 + 1 = 1
                if(node.left != null){
                    q.offer(new Pair(node.left, cur_id*2+1));
                }
                //right child will have 0*2 + 2  = 2...and so on 
                if(node.right != null){
                    q.offer(new Pair(node.right, cur_id*2+2));
                }
            }
            
            //update res with max(res, last(max/rightmostIdx)-first(leftmostIdx) + 1)
            //sanity check - for a parent node say 1, at index 0, 
            //so last,first = 0-> 0-0+1 = 1
            //since we travelled just 1 node, so width= (0-0+1) =  1
            //so last-first+1 will give max width of the tree
            res = Math.max(res, last - first + 1);
        }
        
        return res;    
    }
}
