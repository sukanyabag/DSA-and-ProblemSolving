class BinaryTree: # O(1) time & O(N) space.
    def __init__(self, size):
        self.customList = size * [None]
        self.maxsize = size
        self.lastUsedIdx = 0

    def insertNode(self, value): # O(1) time & O(1) space.
        if self.lastUsedIdx + 1 == self.maxsize:
            return "The Binary Tree is full."
        self.customList[self.lastUsedIdx + 1] = value
        self.lastUsedIdx += 1
        return "The node has been successfully inserted."
    
    def searchNode(self, nodevalue): # O(N) time & O(1) space.
        for i in range (len(self.customList)):
            if self.customList[i] == nodevalue:
                return "Node found!"
            else:
                return "Node not found!"
     
    '''TRAVERSAL (ALL KINDS) -> TIME - O(N),SPACE- O(1)'''

    def preOrderTraversal(self, idx): # O(N) time & O(N) space.
        if idx > self.lastUsedIdx:
            return
        print(self.customList[idx]) #root
        self.preOrderTraversal(idx*2) #left
        self.preOrderTraversal(idx*2 + 1) #right

    def inOrderTraversal(self,idx): # O(N) time & O(N) space.
        if idx > self.lastUsedIdx:
            return
        self.inOrderTraversal(idx*2) #left
        print(self.customList[idx]) #root
        self.inOrderTraversal(idx*2 + 1) #right
    
    def postOrderTraversal(self,idx): # O(N) time & O(N) space.
        if idx > self.lastUsedIdx:
            return
        self.postOrderTraversal(idx*2) #left
        self.postOrderTraversal(idx*2 + 1) #right
        print(self.customList[idx]) #root

    def levelOrderTraversal(self,idx): # O(N) time & O(N) space.
        for i in range(idx, self.lastUsedIdx+1):
            print(self.customList[i])

    def deleteNode(self, value): # O(N) time & O(N) space.
        if self.lastUsedIdx == 0:
            return "No node found to be deleted."
        # a)find the value we want to delete
        #b) replace that value with the value of deepest node(here, deepest node =lastindex)
        #c) finally delete the deepest node from the binary tree
        for i in range(1, self.lastUsedIdx+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIdx]
                self.customList[self.lastUsedIdx] = None
                self.lastUsedIdx -= 1
                return "The node has been successfully deleted."
    
    def deleteBT(self): # O(1) time & O(1) space.
        self.customList = None
        return "The binary tree has been deleted!"

    
newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.searchNode("Tea"))
newBT.preOrderTraversal(1)
newBT.inOrderTraversal(1)
newBT.postOrderTraversal(1)
newBT.levelOrderTraversal(1)
