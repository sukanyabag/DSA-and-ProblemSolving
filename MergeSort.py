#helper funtion for merging
def merge(customList, left, mid, right):
    #number of elements in 1st subarray
    n1 = mid - left + 1
    n2 = right - mid
    
    # creating subarray 
    left_subarray = [0] * n1
    right_subarray = [0] * n2
    
    # copying values from customlist to subarrays
    for i in range(0,n1):
        left_subarray[i] = customList[left + i]

    for j in range(0,n2):
        right_subarray[j] = customList[mid + 1 + j]


    # initial indexes
    i = 0 #index of left subarray
    j = 0 #index of right subarray
    k = left # index of merged list

    #loop to perform merging after sorting
    while i < n1 and j < n2:
        if left_subarray[i] <= right_subarray[j]:
            customList[k] = left_subarray[i]
            i += 1
        else:
            customList[k] = right_subarray[j]
            j += 1

        k += 1

    #loop for copying remaining element of left_subarray
    while i < n1:
        customList[k] = left_subarray[i]
        i += 1
        k += 1
    #loop for copying remaining element of right_subarray
    while j < n2:
        customList[k] = right_subarray[j]
        j += 1
        k += 1

#merge sort function
def mergeSort(customList, left, right):#time - O(NlogN), SPACE- O(N)
    if left < right:
        mid = (left + (right-1))//2
        mergeSort(customList, left, mid)
        mergeSort(customList, mid+1, right)
        merge(customList, left, mid, right)
    return customList

#check how it works
cList = [2,1,7,6,5,3,4,9,8]
print(mergeSort(cList, 0, 8))
