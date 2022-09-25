'''
Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
The efficient way is the one that involves the least number of multiplications.

The dimensions of the matrices are given in an array arr[] of size N (such that N = number of matrices + 1)
where the ith matrix has the dimensions (arr[i-1] x arr[i]).

Expected Time Complexity: O(N3)
Expected Auxiliary Space: O(N2)

Memoized Solution
'''
class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[-1 for _ in range(N)] for _ in range(N)]
        i = 1
        j = N - 1
        return self.helper(arr, i, j, dp)

    def helper(self, arr, i, j, dp):
        if i == j:
            return 0
            
        if dp[i][j]!=-1:
            return dp[i][j]
        
        mini = float("inf")
        for k in range(i, j):
            ans = self.helper(arr, i, k, dp) + self.helper(arr, k + 1, j, dp) + arr[i-1] * arr[k] * arr[j]
            mini = min(mini, ans)
        return mini

