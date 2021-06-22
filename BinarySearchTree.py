class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue): #Time - O(logN) Space-O(logN)

        if rootNode.data == None:
            rootNode.data = nodeValue
        elif nodeValue <= rootNode.data:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(nodeValue)
            else:
                insertNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(nodeValue)
            else:
                insertNode(rootNode.rightChild, nodeValue)

        return "The node is succesfully inserted in the BST!"

def preOrderTraversal(rootNode): #Time - O(N) Space-O(N)

    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def InOrderTraversal(rootNode): #Time - O(N) Space-O(N)

    if not rootNode:
        return
    InOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    InOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode): #Time - O(N) Space-O(N)

    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

from collections import deque as queue
from typing import MutableMapping
def levelOrderTraversal(rootNode): #Time - O(N) Space-O(N)
    if not rootNode:
        return
    # Create an empty queue for
    # level order traversal
    q = queue()
    # To store front element of
    # queue.
    #node *curr
  
    # Enqueue Root and None node.
    q.append(rootNode)
    q.append(None)
    while (len(q) > 1):
        curr = q.popleft()
        # Condition to check
        # occurrence of next
        # level.
        if (curr == None):
           q.append(None)
           print()
        else:
            # Pushing left child of
            # current node.
            if (curr.leftChild):
                q.append(curr.leftChild)
            # Pushing right child of
            # current node.
            if (curr.rightChild):
                q.append(curr.rightChild)
            print(curr.data, end = " ")

def searchNode(rootNode, nodeValue): #Time - O(logN) Space-O(logN)
    try:
        if rootNode.data == nodeValue:
            print(f"The value {nodeValue} is found at the root of the BST!")

        
        elif nodeValue < rootNode.data:
            if rootNode.leftChild.data == nodeValue:
                print(f"The value {nodeValue} is found in the BST!")
            else:
                searchNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild.data == nodeValue:
                print(f"The value {nodeValue} is found in the BST!")
            else:
               searchNode(rootNode.rightChild, nodeValue)

    except AttributeError:
        print(f"The value {nodeValue} does not exist in the BST! Please enter a valid entry!")
    
#helper func for deleting a node which has two children(can be parent too)
def minValueNode(bstNode):
    curr = bstNode
    while (curr.leftChild is not None):
        curr = curr.leftChild
    return curr

def deleteNode(rootNode, nodeValue): #Time - O(logN) Space-O(logN)
    #0th case -base-case
    if rootNode is None:
        return rootNode
    # 1st case - the node to be deleted is a leaf node
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue) #recursively call until leaf reached
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue) #recursively call until leaf reached
    # 2nd case - the node to be deleted has only 1 child node (can be parent too)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
    # 3rd case - the node to be deleted has 2 children (can be parent too)
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode): #Time - O(1) Space-O(1)
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return " The Binary Search Tree has been deleted!"

#Create a BST object - Time - O(1) Space-O(1)
newBST = BSTNode(None) 

insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)


preOrderTraversal(newBST)
InOrderTraversal(newBST)
postOrderTraversal(newBST)
levelOrderTraversal(newBST)
searchNode(newBST, 10)
deleteNode(newBST, 90)
levelOrderTraversal(newBST)