'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by 
increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
Find out the minimum possible difference of the height of shortest and longest towers after you have modified each tower.

Note: It is compulsory to increase or decrease by K to each tower.
Example 1:
Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.

our Task:
You don't need to read input or print anything. 
Your task is to complete the function getMinDiff() which takes the arr[], n and k as input parameters and returns an integer denoting the minimum difference.

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)

Constraints
1 ≤ K ≤ 104
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 105
'''
#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        #sorts arr in ascending order
        arr.sort()
        
        #minimum possible difference of the height
        min_diff = arr[n-1] - arr[0]
        
        #initialize tmp_min and tmp_max
        tmp_min = arr[0]
        tmp_max = arr[n-1]
        
        for i in range(1,n):
            tmp_min = min(arr[0]+k, arr[i]-k)
            tmp_max = max(arr[i-1]+k, arr[n-1]-k)
            
            if (tmp_max >= 0 and tmp_min >= 0):
                min_diff = min(min_diff, tmp_max - tmp_min)
                
            
        return min_diff
        
        

'''
JAVA - 
/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

	// User function Template for Java
	public static int getMinDiff(int[] arr, int n, int k)
	{

		Arrays.sort(arr);
		// Maximum possible height difference
		int ans = arr[n - 1] - arr[0];

		int tempmin, tempmax;
		tempmin = arr[0];
		tempmax = arr[n - 1];

		for (int i = 1; i < n; i++) {

			// if on subtracting k we got negative then
			// continue
			if (arr[i] - k < 0)
				continue;

			// Minimum element when we add k to whole array
			tempmin = Math.min(arr[0] + k, arr[i] - k);

			// Maximum element when we subtract k from whole
			// array
			tempmax
				= Math.max(arr[i - 1] + k, arr[n - 1] - k);
            if(tempmax>=0 && tempmin>=0){
			  ans = Math.min(ans, tempmax - tempmin);
          }
		}
		return ans;
	}
}
