/*
Given a Binary Tree, convert it into its mirror.
*/

// User function Template for Java

// function Template for Java

// FUNCTION CODE
/* A Binary Tree node
class Node
{
    int data;
    Node left, right;
   Node(int item)
   {
        data = item;
        left = right = null;
    }
} */

class Solution {
    // Function to convert a binary tree into its mirror tree.
    Node mirror(Node node) {
        // Your code here
        if(node == null) return null;
        
        //do the subtrees with recursive calls
        Node left = mirror(node.left);
        Node right = mirror(node.right);
        
        //invert by swapping the left and right pointers
        node.left = right;
        node.right = left;
        
        return node;
    }
}
