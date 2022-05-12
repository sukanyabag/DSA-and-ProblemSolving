'''
An array contains both positive and negative numbers in random order.
Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
Note: Order of elements is not important here.
'''

def moveNegatives(arr, n ):
    j = 0
    for i in range(0, n) :
        if (arr[i] < 0) :
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    print(arr)
