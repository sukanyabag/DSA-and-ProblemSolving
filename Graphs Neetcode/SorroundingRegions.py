'''
3 strategies to follow while solving a bit flipping/char flipping problem like this-
Apply reverse thinking pattern-
Here, we are asked to capture only sorrounded regions-
Applying reverse thinking, we solve like this -> capture everything except unsorrounded regions.
This makes things easier, let's see how..

Here, every unsorrounded region is at the boundary/edge. So scan every edge and flag them
so that we avoid them while capturing.

Let's explain the major 3 steps to solve this problem-
#1. DO A DFS TRAVERSAL AND FLAG ALL UNSORROUNDED/EDGE REGIONS WITH F.(O->F)
#2. NOW RELAX AND CAPTURE THE SORROUNDED REGIONS. (O->X)
#3. RESET/UNCAPTURE/REMOVE FLAGS FROM UNSORROUNDED REGIONS. (F->O)

AFTER THIS THE FINAL BOARD WILL BE captured by flipping all 'O's into 'X's in that surrounded region.
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        def captureBydfs(r,c):
            #base/edge check
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return
            
            #flag
            board[r][c] = "F"
            
            #capture
            captureBydfs(r + 1, c)
            captureBydfs(r - 1, c)
            captureBydfs(r, c + 1)
            captureBydfs(r, c - 1)
            
        #1 CALL DFS TRAVERSAL(captureBydfs) AND FLAG ALL UNSORROUNDED REGIONS WITH F.(O->F)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    captureBydfs(r, c)
                    
        #2 NOW RELAX AND CAPTURE THE SORROUNDED REGIONS. (O->X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        #3 RESET/UNCAPTURE/REMOVE FLAGS FROM UNSORROUNDED REGIONS. (F->O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "F":
                    board[r][c] = "O"
                    
            
            
            
            
