'''
Question - Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
Example 1:
Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.

Your Task:
You don't need to read input or print anything. 
Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 10^6
0 <= A[i] <= 2
'''

#User function Template for python3
# 1, 0, 2 
# 2nd iteration -> (low,mid swap)- 0,1,2 
#so, low = 1, mid = 1+1=2, high = 2
# mid == high -> arr[mid=2]= 2 -> mid-high swap-> arr[mid] = arr[high]-> no swap 
#end result - [0,1,2]
class Solution:
    def sort012(self,arr,n):
        # code here
        low = 0
        mid = 0 # 0+1 = 1
        high = n-1 # 3-1 = 2 
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1 
                
            elif arr[mid] == 1:
                mid += 1
                
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high = high - 1
        
        return arr
                
                
