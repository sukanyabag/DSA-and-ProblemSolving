'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. 
You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array,
then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
'''
#MEMOIZATION, TC - O(N^3), SC - O(N^2) + AUXX STACK SPACE

from functools import cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]
   
        @cache
        def dfs(l,r):
            if l > r:
                return 0
            
            if dp[l][r] != -1:
                return dp[l][r]
            
            #dp[(l,r)] = 0
            
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(i+1,r) + dfs(l, i-1)
                dp[l][r] = max(dp[l][r], coins)
                
            return dp[l][r]
        
        return dfs(1, n - 2)
      
      
 #TABULATION (TC SAME, SC - NO AUX STACK SPACE)
class Solution:
    def maxCoins(self, A):
        A, n = [1] + A + [1], len(A) + 2
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = max(A[i]*A[k]*A[j] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
        
        return dp[0][n-1]
