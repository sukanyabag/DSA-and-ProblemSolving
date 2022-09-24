'''
Given an array of n positive integers. Find the sum of the maximum sum subsequence of the given array such that the integers in the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence. 

Example 1:

Input: N = 5, arr[] = {1, 101, 2, 3, 100} 
Output: 106
Explanation:The maximum sum of a
increasing sequence is obtained from
{1, 2, 3, 100}
'''
#just tweaked LIS code
#User function Template for python3
#TABULATED CODE
class Solution:
	def maxSumIS(self, arr, n):
		# code here
		dp = [0] * n
	
		#compute msis in bottom up manner aka tabulation
		for i in range(n):
		    #init msis for all indices
		    dp[i] = arr[i]
		    #msis subproblems
		    for j in range(i):
		        if(arr[i] > arr[j]):
		            dp[i] = max(dp[i], dp[j] + arr[i])
		            
		return max(dp)
		       
