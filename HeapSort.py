#helper function - heapify to store properties of binary heap
def heapify(customList, n_elements, idx):
    smallest = idx
    # find left and right child of i
    left = 2*idx + 1
    right = 2*idx + 2

    if left < n_elements and customList[left] < customList[smallest]:
        smallest = left
        
    if right < n_elements and customList[right] < customList[smallest]:
        smallest = right

    if smallest != idx:
        customList[idx] , customList[smallest] = customList[smallest], customList[idx]
        heapify(customList, n_elements, smallest)

def heapSort(customList): #time - O(NlogN), SPACE- O(1)

    n_elements = len(customList)

    for idx in range(int(n_elements/2)-1, -1, -1):
        heapify(customList,n_elements,idx)

    for idx in range(n_elements-1, 0 , -1):
        customList[idx] , customList[0] = customList[0], customList[idx]
        heapify(customList, idx, 0)
    customList.reverse()

#check how it works
cList = [2,1,7,6,5,3,4,9,8]
heapSort(cList)
print(cList)



