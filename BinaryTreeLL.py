
'''
Q- Implement a binary tree using Linked List data structure and oop.
'''
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

#creating tree

newBT = TreeNode("Drinks") #time and space is O(1)
leftChild = TreeNode("Hot")
tea = TreeNode('Tea')
coffee= TreeNode('Coffee')
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild  = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

# create and call pre-order traversal function recursively

def preOrderTraversal(rootNode): #time and space is O(N)
    if not rootNode:
        return #--- O(1)
    print(rootNode.data) #--- O(1)
    preOrderTraversal(rootNode.leftChild) #--- O(n/2) (for each children there are two nodes)
    preOrderTraversal(rootNode.rightChild) #--- O(n/2) (for each children there are two nodes)

#sanity check
preOrderTraversal(newBT)

def inOrderTraversal(rootNode): #time and space is O(N)
    if not rootNode:
        return #--- O(1)
    inOrderTraversal(rootNode.leftChild) #--- O(n/2) (for each children there are two nodes)
    print(rootNode.data) #--- O(1)
    inOrderTraversal(rootNode.rightChild) #--- O(n/2) (for each children there are two nodes)

#sanity check
inOrderTraversal(newBT)

def postOrderTraversal(rootNode): #time and space is O(N)
    if not rootNode:
        return #--- O(1)
    postOrderTraversal(rootNode.leftChild) #--- O(n/2) (for each children there are two nodes)
    postOrderTraversal(rootNode.rightChild) #--- O(n/2) (for each children there are two nodes)
    print(rootNode.data) #--- O(1)

#sanity check
postOrderTraversal(newBT)

'''
Note - 
For level order traversal, we need to take the help of queue data structure
(since queue works as fifo), with linked list for implmenting l-o-t in binary tree.
For simplicity I will import the QueueLinkedList module which has already been coded by me earlier 
while learning queue ds.
'''
from typing import Generator
import QueueLinkedList as q

def levelOrderTraversal(rootNode): #time and space is O(N)
    if not rootNode:
        return
    else:
        customQueue = q.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

levelOrderTraversal(newBT)

def searchBT(rootNode, nodeValue): #time and space is O(N)
    if not rootNode:
        return "The Binary Tree doesn't exist."
    else:
        customQueue = q.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Successfully found the node!"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Value not found!"

print(searchBT(newBT, "cola"))
print(searchBT(newBT, "Tea"))

def insertNodeBT(rootNode, newNode): #time and space is O(N)
    #base
    if not rootNode:
        rootNode = newNode
    #use level-order traversal and insert newnode in left child of 1st vacant node of that level
    else:
        customQueue = q.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted newnode!"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted newnode!"

newNode = TreeNode("Cola")
print(insertNodeBT(newBT, newNode))

#helper 1 for node deletion
def getDeepestNode(rootNode):
    if not rootNode:
        return 
    else:
        customQueue = q.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

deepestNode = getDeepestNode(newBT)
print(deepestNode.data)

#helper 2 for node deletion
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = q.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

newNode = getDeepestNode(newBT)
deleteDeepestNode(newBT, newNode)
levelOrderTraversal(newBT)

def deleteNodeBT(rootNode, node): #time and space is O(N)
     if not rootNode:
         return "The Binary Tree doesn't exist."
     else:
         customQueue = q.Queue()
         customQueue.enqueue(rootNode)
         while not(customQueue.isEmpty()):
             root = customQueue.dequeue()
             if (root.value.data == node):
                 dNode = getDeepestNode(rootNode)
                 root.value.data = dNode.data
                 deleteDeepestNode(rootNode, dNode)
                 return "The node has been successfully deleted."
             if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
             if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
         return "Failed to delete the node!"

deleteNodeBT(newBT, "Tea")
levelOrderTraversal(newBT)

def deleteBT(rootNode): #time is O(1) and space is O(1)
    rootNode.data = None
    rootNode.leftChild =  None
    rootNode.rightChild = None
    return "The Binary Tree has been succesfully deleted."
















