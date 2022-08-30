/*
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary 
tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
Accepted
833,934
Submissions
1,386,816
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
 
 1. init a preOrdidx pointer
 2. in function buildTree, init preOrdidx as 0, init the inorder hashmap <val, idx>
 3. then loop over and put every elm and their idx from inorder array to hmap
 4. start helper function arraytoTree which takes in preorder array, and treenodes left and right
 5. if there are no elm to construct the tree (left > right) return null
 6. select preOrdidx element as root in a new variable and increment it
 7. add that to a new var treenode root
 8. then build the left and right subtree excluding inorderIndexMap[rootValue]
 9. return root
 10. dont forget to call this helper in the main function from 0 to preorder length - 1
 */
class Solution {
    //init a preOrdidx pointer
    int preOrdIdx;
    HashMap<Integer, Integer> inordIdxMap;
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
      //in function buildTree, init preOrdidx as 0, init the inorder hashmap <val, idx>
        preOrdIdx = 0;
        inordIdxMap =  new HashMap<>();
        
      //then loop over and put every elm and their idx from inorder array to hmap
        for(int i = 0; i < inorder.length; i++){
            inordIdxMap.put(inorder[i], i);
        }
      
      //call this helper arrayTOtree in the main function from 0 to preorder length - 1
        return arrayTOtree(preorder, 0, preorder.length - 1);
    }
    
 // start helper function arraytoTree which takes in preorder array, and treenodes left and right
    private TreeNode arrayTOtree(int[] preorder, int left, int right){
        //no elm  to construct tree - base case
        // if there are no elm to construct the tree (left > right) return null
        if(left > right) return null;
        
      // select preOrdidx element as root in a new variable and increment it
        int rootVal = preorder[preOrdIdx++];
        
      //add that to a new var treenode root
        TreeNode root = new TreeNode(rootVal);
        
      // build the left and right subtree excluding inorderIndexMap[rootValue]
        root.left = arrayTOtree(preorder, left, inordIdxMap.get(rootVal) - 1);
        root.right = arrayTOtree(preorder, inordIdxMap.get(rootVal) + 1, right);
        
      // return root
        return root;
        
    }
}

//PYTHON VERSION - 
 class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        
        root = TreeNode(preorder[0])
        pivot = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1: pivot+1], inorder[:pivot])
        root.right = self.buildTree(preorder[pivot+1: ], inorder[pivot+1: ])
        
        return root
