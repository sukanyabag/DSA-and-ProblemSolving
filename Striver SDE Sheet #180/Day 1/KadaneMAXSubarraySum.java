/*
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
Example 1:
Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Your Task:
You don't need to read input or print anything. 
The task is to complete the function maxSubarraySum() which takes Arr[] and N as input parameters and returns the sum of subarray with maximum sum.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 106
-107 ≤ A[i] ≤ 107
*/
class Solution{

    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    long maxSubarraySum(int arr[], int n){
        
        // Your code here
        //maxsum should be initialized to arr[0] so that it doesn't give 0 
        //when we have negative numbers in arr
        
        int maxsum = arr[0];
        int currsum = 0;
        
        for(int i = 0; i<n; i++){
            //subarr sums
            currsum += arr[i];
            
            if(currsum > maxsum){
                //update maxsum to currsum if currsum is greater than maxsum
                maxsum = currsum;
            }
            
            if(currsum < 0){
               //if currsum is -ve, reset it to 0
                currsum = 0;
            }
            
        }
        
        return maxsum;
    }
    
}
