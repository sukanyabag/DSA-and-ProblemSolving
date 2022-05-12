'''
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
'''
#User function Template for python3
from sys import maxsize
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        int_min = -maxsize-1
        max_so_far = int_min
        max_curr = 0
        
        for i in range(0,N):
            max_curr = max_curr + arr[i]
            if (max_so_far < max_curr):
                max_so_far = max_curr
            
            #ignore max_curr and set it to 0 when it's less than 0
            if max_curr < 0:
                max_curr = 0
                
        return max_so_far

