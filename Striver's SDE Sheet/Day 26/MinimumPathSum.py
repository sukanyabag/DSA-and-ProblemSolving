'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''
#TABULATED BOTTOM UP DP APPROACH
#TC - O(M*N)
#SC - O(M*N)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        dp = [[float("inf")]* (cols+1) for r in range(rows+1)]
        
        dp[rows-1][cols] = 0
        
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                #down = dp[r+1][c], right =  dp[r][c+1]
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
                
        return dp[0][0]
        
