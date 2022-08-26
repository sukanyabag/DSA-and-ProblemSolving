/*
Post-Order Traversal Of Binary Tree - [LEFT,RIGHT,ROOT]
Problem Statement: Postorder Traversal of a binary tree. Write a program for the postorder traversal of a binary tree.
*/
//RECURSIVE - O(N) TIME, O(N) SPACE
public class Solution {
    static void postOrderTrav(Node curr, ArrayList < Integer > postOrder) {
        if (curr == null)
            return;

        postOrderTrav(curr.left, postOrder);
        postOrderTrav(curr.right, postOrder);
        postOrder.add(curr.data);
    }
  
 //ITERTATIVE - USING SINGLE STACK
  
/*
Intuition: First we need to understand what we do in a postorder traversal. 
We first explore the left side of the root node and keep on moving left until we encounter a node pointing to NULL. 
As now there is nothing more to traverse on the left, we move to the immediate parent(say node P) of that NULL node.
Now we again start our left exploration from the right child of that node P. 
We will print a node’s value only when we have returned from its both children.

Approach:
The algorithm steps can be stated as:
We take an explicit data structure and a cur pointer pointing to the root of the tree.

We run a while loop till the time the cur is not pointing to NULL or the stack is non-empty.

If cur is not pointing to NULL, it means then we simply push that value to the stack and move the cur pointer to its left child 
because we want to explore the left child before the root or the right child.

If the cur is pointing to NULL, it means we can’t go further left, then we take a variable temp and set it to  cur’s parent’s right child
(as we have visited the left child, now we want to visit the right child). We have node cur’s parent at the top of the stack.

If node temp is not pointing to NULL, we simply initialise cur as node temp so that 
we can again start looking at the left of node temp from the next iteration.

If node temp is pointing to NULL, then first of all we are sure that we have visited both children of temp’s parent,
so it’s time to print it. Therefore we set temp to its parent( present at the top of stack), pop the stack and then print temp’s value.

Additionally,  this new temp(parent of NULL-pointing node) can be the right child of the node present at the top of stack after popping.
In that case the node at top of the stack is parent of temp and the next node to be printed. Therefore we run an additional while loop to check 
if that is the case, if true then again move temp to its parent and print its value.
*/
  
public class Solution {
    static ArrayList < Integer > postOrderTrav(Node cur) {

        ArrayList < Integer > postOrder = new ArrayList < > ();
        if (cur == null) return postOrder;

        Stack < Node > st = new Stack < > ();
        while (cur != null || !st.isEmpty()) {

            if (cur != null) {
                st.push(cur);
                cur = cur.left;
            } else {
                Node temp = st.peek().right;
                if (temp == null) {
                    temp = st.peek();
                    st.pop();
                    postOrder.add(temp.data);
                    while (!st.isEmpty() && temp == st.peek().right) {
                        temp = st.peek();
                        st.pop();
                        postOrder.add(temp.data);
                    }
                } else cur = temp;
            }
        }
        return postOrder;


    }
