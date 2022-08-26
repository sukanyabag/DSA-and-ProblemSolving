/*
Inorder Traversal of Binary Tree
Problem Statement: Given a Binary Tree. Find and print the inorder traversal of Binary Tree.
*/

Iterative - inorder -> [Left -> Root -> Right]
Stack is a Last-In-First-Out (LIFO) data structure, therefore when we encounter a node, we simply push it to the stack and try to find nodes on its left.
When the current node points to NULL, it means that there is nothing left to traverse and we should move to the parent.
This parent is always placed at the top of the stack. If the stack is empty, then we had already traversed the whole tree and should stop the execution.
  
The algorithm approach can be stated as:
1.We first take an explicit stack data structure and set an infinite loop.
2.In every iteration we check whether our current node is pointing to NULL or not.
3.If it is not pointing to NULL, we simply push the current value to the stack and move the current node to its left child.
4.If it is pointing to NULL, we first check whether the stack is empty or not. If the stack is empty, it means that we have traversed the tree and we BREAK out of the loop.
5.If the stack is not empty, we pop the top value of the stack, print it and move the current node to its right child.
  
 class Solve {
    static ArrayList < Integer > inOrderTrav(Node curr) {
        ArrayList < Integer > inOrder = new ArrayList < > ();
        Stack < Node > s = new Stack < > ();
        while (true) {
            if (curr != null) {
                s.push(curr);
                curr = curr.left;
            } else {
                if (s.isEmpty()) break;
                curr = s.peek();
                inOrder.add(curr.data);
                s.pop();
                curr = curr.right;
            }
        }
        return inOrder;
    }
   
  Recursive-
   
    class Solve {

    static void inOrderTrav(Node root, ArrayList < Integer > inOrder) {
        if (root == null)
            return;

        inOrderTrav(root.left, inOrder);
        inOrder.add(root.val);
        inOrderTrav(root.right, inOrder);
    }

   
