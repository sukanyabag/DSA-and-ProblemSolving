/* 
Question - 
Given an array arr[] and an integer K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
Example 1:
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.
Example 2:

Your Task:
You don't have to read input or print anything. 
Your task is to complete the function kthSmallest() which takes the array arr[], integers l and r denoting 
the starting and ending index of the array and an integer K as input and returns the Kth smallest element.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(log(n))
Constraints:
1 <= N <= 105
1 <= arr[i] <= 105
1 <= K <= N
*/

import java.util.Arrays;
import java.util.Collections;

class Solution{
    public static int kthSmallest(Integer[] arr, int k) 
    { 
        //Your code here
        Arrays.sort(arr);
        
        return arr[k-1];
    } 
}



#python3
def kthSmallest(arr, n, k):
 
    # Sort the given array
    arr.sort()
 
    # Return k'th element in the
    # sorted array
    return arr[k-1]
