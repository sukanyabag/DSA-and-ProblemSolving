import math
from InsertionSort import insertionSort

def bucketSort(customList): #time - O(N^2), SPACE- O(N)
    n_buckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)

    temp_arr = []

    for i in range(n_buckets):
        temp_arr.append([]) #buckets
    
    for j in customList:
        indexOfBucket = math.ceil(j * n_buckets / maxValue)
        #inserts element in appropriate bucket, starting from 0th index
        temp_arr[indexOfBucket-1].append(j) 

    for i in range(n_buckets):
        temp_arr[i] = insertionSort(temp_arr[i])

    #merge sorted buckets
    k = 0
    for i in range(n_buckets):
        for j in range(len(temp_arr[i])):
            customList[k] = temp_arr[i][j]
            k += 1
    return customList

cList = [2,1,7,6,5,3,4,9,8]
print(bucketSort(cList))
        

