/*
Preorder Traversal of Binary Tree - [ROOT -> LEFT -> RIGHT]
Problem Statement: Given a binary tree print the preorder traversal of binary tree.

Solution 1: Iterative
Intuition: In preorder traversal, the tree is traversed in this way: root, left, right.
When we visit a node, we print its value, and then we want to visit the left child followed by the right child. 
The fundamental problem we face in this scenario is that there is no way that we can move from a child to a parent. 
To solve this problem, we use an explicit stack data structure. 
While traversing we can insert node values to the stack in such a way that we always get the next node value at the top of the stack.

Approach: 
The algorithm approach can be stated as:
1. We first take an explicit stack data structure and push the root node to it.(if the root node is not NULL).
2. Then we use a while loop to iterate over the stack till the stack remains non-empty.
3. In every iteration we first pop the stack’s top and print it. 
4. Then we first push the right child of this popped node and then push the left child, if they are not NULL. We do so because stack is a last-in-first-out(LIFO) data structure. We need to access the left child first, so we need to push it at the last.
5. The execution continues and will stop when the stack becomes empty. In this process, we will get the preorder traversal of the tree.

*/
public class Solution {
    static ArrayList < Integer > preOrderTrav(Node curr) {
        ArrayList < Integer > preOrder = new ArrayList < Integer > ();
        if (curr == null)
            return preOrder;

        Stack < Node > s = new Stack < > ();
        s.push(curr);

        while (!s.isEmpty()) {
            Node topNode = s.peek();
            preOrder.add(topNode.data);
            s.pop();
            if (topNode.right != null)
                s.push(topNode.right);
            if (topNode.left != null)
                s.push(topNode.left);
        }
        return preOrder;

    }

  
Recursive- 
 public class Solution {
    static void preOrderTrav(Node curr, ArrayList < Integer > preOrder) {
        if (curr == null)
            return;

        preOrder.add(curr.data);
        preOrderTrav(curr.left, preOrder);
        preOrderTrav(curr.right, preOrder);
    }


  
