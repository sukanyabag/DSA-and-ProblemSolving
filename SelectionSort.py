def selectionSort(customList): #time - O(N^2), SPACE- O(1)
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i] , customList[min_index] = customList[min_index], customList[i]
    print(customList)

cList = [2,1,7,6,5,3,4,9,8]
selectionSort(cList)