/*
Problem Statement: BoundaryTraversal of a binary tree. Write a program for the Anti-Clockwise Boundary traversal of a binary tree.
Approach: Boundary traversal in an anti-clockwise direction can be described as a traversal consisting of three parts:
Part 1: Left Boundary of the tree (excluding the leaf nodes).
Part 2: All the leaf nodes travelled in the left to right direction.
Part 3: Right Boundary of the tree (excluding the leaf nodes), traversed in the reverse direction.
*/

public class Main {
   //this function checks if its a leaf node
    static Boolean isLeaf(Node root) {
        return (root.left == null) && (root.right == null);
    }
    //this function adds left boundary in the following way
    //start from root.left by setting current to root.left
    // unless current becomes null -> if its not a leaf node, add it to result
    //keep on traversing left children, if left exhausted, traverse right
    static void addLeftBoundary(Node root, ArrayList < Integer > res) {
        Node cur = root.left;
        while (cur != null) {
            if (isLeaf(cur) == false) res.add(cur.data);
            if (cur.left != null) cur = cur.left;
            else cur = cur.right;
        }
    }
  
    //this function adds right boundary in the following way
    //start from root.right by setting current to root.right
    //init a temp data structure
    // unless current becomes null -> if its not a leaf node, add it to temp
    //keep on traversing right children, if right exhausted, traverse left
    static void addRightBoundary(Node root, ArrayList < Integer > res) {
        Node cur = root.right;
        ArrayList < Integer > tmp = new ArrayList < Integer > ();
        while (cur != null) {
            if (isLeaf(cur) == false) tmp.add(cur.data);
            if (cur.right != null) cur = cur.right;
            else cur = cur.left;
        }
      //now back traverse the temp ds to add right subtree in reverse fashion to result
        int i;
        for (i = tmp.size() - 1; i >= 0; --i) {
            res.add(tmp.get(i));
        }
    }
    
   //this function adds leaf nodes 
   //hence if its a leaf node, add it to res
    static void addLeaves(Node root, ArrayList < Integer > res) {
        if (isLeaf(root)) {
            res.add(root.data);
            return;
        }
        if (root.left != null) addLeaves(root.left, res);
        if (root.right != null) addLeaves(root.right, res);
    }
  
    //main function that calls all the 3 rules required for boundary traversal
    static ArrayList < Integer > printBoundary(Node node) {
        //init arraylist that stores answer
        ArrayList < Integer > ans = new ArrayList < Integer > ();
        //if not leaf node add node value to answer
        if (isLeaf(node) == false) ans.add(node.data);
        //rule 1 -add left boundaries excluding leaf
        addLeftBoundary(node, ans);
        //rule 2 - add leaf nodes
        addLeaves(node, ans);
        //rule 3 - add right bundaries in reverse order excluding leaf
        addRightBoundary(node, ans);
        //return entire boundary traversal
        return ans;
    }
