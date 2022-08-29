/**
Google version -  Consider a binary tree of N vertices such that children of node k are 2*k and 2*k+1. 
Vertex 1 is the root of the tree and each node has an integer value associated with it.
Such a tree may be represented as an array of N integers by writing down values from consecutive nodes.

The tree can be represented as an array [-1, 7, 0, 7, -8].
A node is said to be at level x if the length of the shortest path between that node and root x-1. So, the root is at level 1, the children of root are at level 2, and so on.

Your task is to find the smallest level number x such that sum of all nodes at level x is maximal.
Examples: Given array A such that: A[0]=-1, A[1]=7, A[2]=0, A[3]=7, A[4]=-8. The function should return 2.


Leetcode version - Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
**/

class Solution {
    public int maxLevelSum(TreeNode root) {
        //base case
        if(root == null) return 0;
        
        //init queue
        Queue<TreeNode> q = new LinkedList<>();
        
        //add root
        q.offer(root);
        
        //init params
        int level = 0;
        int minLevel = 0;
        int maxSum = Integer.MIN_VALUE;
        
        //loop over until queue is empty
        while(!q.isEmpty()){
            //1st part - getting the necessary params and increasing level everytime
            int size = q.size();
            int levelSum = 0;
            level++;
            
            //loop over from i -> 0 to size of q
            // do bfs traversals on left and right subtrees
            //update the levelSum
            for(int i = 0; i < size; i++){
                TreeNode node = q.poll();
                levelSum += node.val;
                if(node.left != null) q.offer(node.left);
                if(node.right != null) q.offer(node.right);
            }
            
            //compare levelSum with maxSum
            if(levelSum > maxSum){
                maxSum = levelSum;
                minLevel = level;
            }
            
        }
        
        return minLevel;
    }
}
