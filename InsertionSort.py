def insertionSort(customList): #time - O(N^2), SPACE- O(1)
    #compare current element with next element
    for i in range(1, len(customList)):
        #current element -> key
        key = customList[i]
        #prev element
        j = i-1
        #loop to check current element with next element
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -=1
        customList[j+1] = key
    print(customList)

cList = [2,1,7,6,5,3,4,9,8]
insertionSort(cList)
