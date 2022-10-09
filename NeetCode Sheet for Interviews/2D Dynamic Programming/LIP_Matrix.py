'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally 
or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''

#MEMOIZATION
# TC - O(mn)
# SC - O(mn)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = {}
        
        def dfs(r,c,prev):
            if (r < 0 or r == rows or
                c < 0 or c== cols or
                matrix[r][c] <= prev):
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            
            res = 1
            res = max(res, 1 + dfs(r+1,c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r,c-1,matrix[r][c]))
            res = max(res, 1 + dfs(r,c+1,matrix[r][c]))
            
            dp[(r,c)] = res
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1)
        return max(dp.values())
            
