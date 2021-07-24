#bubble sort
def bubbleSort(customList): #time - O(N^2), SPACE- O(1)
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)

    

cList = [2,1,7,6,5,3,4,9,8]
bubbleSort(cList)
