class Heap: # time - O(1) space-O(N)
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

'''PEEKING IN BINARY HEAP'''
def peekHeap(rootNode): # time - O(1) space-O(1)
    if not rootNode:
        return 
    else:
        return rootNode.customList[1]

'''SIZE OF BINARY HEAP'''

def sizeofHeap(rootNode): # time - O(1) space-O(1)
    if not rootNode:
        return
    else:
        return rootNode.heapSize

'''TRAVERSAL IN BINARY HEAP'''

def levelOrderTraversal(rootNode): # time - O(N) space-O(1)
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])

'''INSERTION IN BINARY HEAP'''
#helper function heapify to maintain properties of the binary heap during insertion
def heapify_toInsert(rootNode, idx, heapType): # time - O(logN) space-O(logN)
    parent_idx = int(idx / 2) #left = 2x, right= 2x+ 1, hence root = x, so 2x/2= x, hence we divide idx/2 to fetch parent
    if idx <= 1: #since we skip 0th index for faster calc
        return
    if heapType == "Min":
        #check if curr node is < than its parents
        if rootNode.customList[idx] < rootNode.customList[parent_idx]:
            temp = rootNode.customList[idx]
            rootNode.customList[idx] = rootNode.customList[parent_idx]
            rootNode.customList[parent_idx] = temp
        heapify_toInsert(rootNode, parent_idx, heapType)

    elif heapType == "Max":
        #check if curr node is > than its parents
        if rootNode.customList[idx] > rootNode.customList[parent_idx]:
            temp = rootNode.customList[idx]
            rootNode.customList[idx] = rootNode.customList[parent_idx]
            rootNode.customList[parent_idx] = temp
        heapify_toInsert(rootNode, parent_idx, heapType)

def insertNode(rootNode, nodeValue, heapType): # time - O(logN) space-O(logN)
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is full!"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapify_toInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted to the binary heap!"

'''EXTRACTION IN BINARY HEAP'''
#helper function heapify to maintain properties of the binary heap during extraction
def heapify_toExtract(rootNode, idx, heapType):
    leftIdx = idx * 2
    rightIdx = idx * 2 + 1
    swapChild = 0
    # 1st condition -  check if heapsize is less than leftidx
    if rootNode.heapSize < leftIdx:
        return 
    # 2nd condition - check if heapsize is equal to leftidx and do adjustments(swap) for min & max heap
    elif rootNode.heapSize == leftIdx:
        if heapType == "Min":
            if rootNode.customList[idx] > rootNode.customList[leftIdx]:
                #swap
                temp = rootNode.customList[idx]
                rootNode.customList[idx] = rootNode.customList[leftIdx]
                rootNode.customList[leftIdx] = temp
            return
        else: # condition for max heap
            if rootNode.customList[idx] < rootNode.customList[leftIdx]:
                #swap
                temp = rootNode.customList[idx]
                rootNode.customList[idx] = rootNode.customList[leftIdx]
                rootNode.customList[leftIdx] = temp
            return
    # 3rd condition -  check if there are left as well as right child, then take least element 
    # among them for min, and max element for max
    else:
        if heapType == "Min":
            #find smallest child
            if rootNode.customList[leftIdx] < rootNode.customList[rightIdx]:
                swapChild = leftIdx
            
            else:
                swapChild = rightIdx
            # replace it with parent node
            if rootNode.customList[idx] > rootNode.customList[swapChild]:
                #swap
                temp = rootNode.customList[idx]
                rootNode.customList[idx] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
            
        else:
            #find biggest child
                if rootNode.customList[leftIdx] > rootNode.customList[rightIdx]:
                    swapChild = leftIdx
                else:
                    swapChild = rightIdx
                if rootNode.customList[idx] < rootNode.customList[swapChild]:
                    #swap
                    temp = rootNode.customList[idx]
                    rootNode.customList[idx] = rootNode.customList[swapChild]
                    rootNode.customList[swapChild] = temp
              
        heapify_toExtract(rootNode, swapChild, heapType)
                
                
            # replace it with parent node
            

def extractNode(rootNode, heapType): # time - O(logN) space-O(logN)
    if rootNode.heapSize == 0:
        return 
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapify_toExtract(rootNode, 1, heapType)
        return extractedNode

def deleteEntireBinaryHeap(rootNode):
    rootNode.customList = None
    

newBinaryHeap = Heap(5)
#print(sizeofHeap(newBinaryHeap))
insertNode(newBinaryHeap, 6 , "Max")
insertNode(newBinaryHeap, 9 , "Max")
insertNode(newBinaryHeap, 5 , "Max")
insertNode(newBinaryHeap, 10 , "Max")
extractNode(newBinaryHeap, "Max")
levelOrderTraversal(newBinaryHeap)