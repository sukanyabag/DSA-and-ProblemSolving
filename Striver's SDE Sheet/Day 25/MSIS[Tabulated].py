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
class Solution:
	def maxSumIS(self, arr, n):
		# code here
		maxsum = 0
		dp = [0 for x in range(n)]
		
		#init msis for all indices
		for i in range(n):
		    dp[i] = arr[i]
		    
		#compute msis in bottom up manner aka tabulation
		for i in range(1,n):
		    for j in range(i):
		        if(arr[i] > arr[j] and dp[i] < dp[j] + arr[i]):
		            dp[i] = dp[j] + arr[i]
		            
		 #traverse dp array and update maxsum, return maxsum
		for i in range(n):
		     if maxsum < dp[i]:
		         maxsum = dp[i]
		         
		         
		return maxsum
