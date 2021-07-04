class AVLNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


'''TRAVERSAL ALGORITHMS'''

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

from collections import deque as queue

def levelOrderTraversal(rootNode): #time complexity - O(N) and space complexity - O(N)
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
        # level
        if curr == None:
            q.append(None)
            print()
        else:
            # Pushing left child of
            # current node.
            if curr.leftChild:
                q.append(curr.leftChild)
            # Pushing right child of
            # current node.
            if (curr.rightChild):
                q.append(curr.rightChild)
            
            print(curr.data, end = " ")

'''SEARCHING ALGORITHM'''

def searchNode(rootNode, nodeValue): #Time - O(logN) Space-O(logN)
    try:
        if rootNode.data == nodeValue:
            print(f"The value {nodeValue} is found at the root of the BST!")

        
        elif nodeValue < rootNode.data:
            if rootNode.leftChild.data == nodeValue:
                print(f"The value {nodeValue} is found in the AVL Tree!")
            else:
                searchNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild.data == nodeValue:
                print(f"The value {nodeValue} is found in the AVL Tree!")
            else:
               searchNode(rootNode.rightChild, nodeValue)

    except AttributeError:
        print(f"The value {nodeValue} does not exist in the AVL Tree! Please enter a valid entry!")

'''INSERTION ALGORITHMS'''

#helper method to get height of nodes before inserting one to avl tree
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

#helper method to rotate right
def rightRotate(disbalancedNode): #time and space - O(1)
    newroot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newroot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newroot.height = 1 + max(getHeight(newroot.leftChild), getHeight(newroot.rightChild))
    return newroot

#helper method to rotate left
def leftRotate(disbalancedNode): #time and space - O(1)
    newroot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newroot.leftChild   = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newroot.height = 1 + max(getHeight(newroot.leftChild), getHeight(newroot.rightChild))
    return newroot

#helper method to check balance
def getBalance(rootNode): #time and space - O(1)
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue): #time and space - O(logN)
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))

    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data: #left-left condition
        return rightRotate(rootNode)
    
    if balance > 1 and nodeValue > rootNode.leftChild.data: #left-right condition
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)

    if balance < -1 and nodeValue > rootNode.rightChild.data: #right-right condition
        return leftRotate(rootNode)

    if balance < -1 and nodeValue < rootNode.rightChild.data: #right-left condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode

'''DELETION ALGORITHMS'''
#helper method to get successor from right subtree before deletion
def getMinValNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue): #time and space - O(logN)
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)

    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = getMinValNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    balance = getBalance(rootNode)

    #LL CONDITION - RIGHT ROTATION
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    #RR CONDITION - LEFT ROTATION
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    #LR CONDITION - LEFT ROTATION + RIGHT ROTATION
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    #RL CONDITION - RIGHT ROTATION + LEFT ROTATION
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def deleteEntireAVL(rootNode): #time and space - O(1)
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL Tree has been deleted!"


newAVLtree = AVLNode(5)
newAVLtree = insertNode(newAVLtree, 10)
newAVLtree = insertNode(newAVLtree, 15)
newAVLtree = insertNode(newAVLtree, 20)
newAVLtree = deleteNode(newAVLtree, 15)
levelOrderTraversal(newAVLtree)



        
