# helper function for partitioning array

#takes last element as pivot and places it in correct position in sorted array
# places all smallr elements than pivot to the left of it and all greater elements to right 

def partition(customList, low, high):
    i = low - 1 #to be used inside loop for swapping vals
    pivot = customList[high]

    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i] , customList[j] = customList[j] , customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)

#quicksort method
def quickSort(customList, low, high): #time - O(NlogN), SPACE- O(N)
    if low < high:
        partition_idx = partition(customList, low, high)
        quickSort(customList, low, partition_idx-1)
        quickSort(customList, partition_idx + 1, high)

#check how it works
cList = [2,1,7,6,5,3,4,9,8]
quickSort(cList, 0, 8)
print(cList)


