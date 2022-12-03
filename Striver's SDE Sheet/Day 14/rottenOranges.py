'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #for bfs
        q = deque()
        
        #to keep track of time and fresh oranges left
        time, fresh = 0,0
        
        #calc len rows and cols
        rows = len(grid)
        cols = len(grid[0])
        
        #if fresh, increment fresh count, if rotten add it to q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])  
                    
        #4-adjacent directions -> up, down, right, left
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
        #this will do bfs until queue is empty and we are out of fresh oranges
        while q and fresh > 0:
            for i in range(len(q)):
                #pop out initial rotten oranges
                r,c = q.popleft()
                
                # do bfs for for every 4 direction
                for dr,dc in dirs:
                    delrow,delcol = dr+r, dc+c
                    
                    #check for boundary conditions
                    if(delrow < 0 or delrow == rows or delcol < 0 or delcol == cols or grid[delrow][delcol] != 1):
                        continue
                    
                    #otherwise if you find fresh oranges make them rotten and add them to q
                    grid[delrow][delcol] = 2
                    q.append([delrow,delcol])
                    #decrement fresh by 1
                    fresh -= 1
            #when loop executes fully, increment time
            time += 1
            
        return time if fresh == 0 else -1
                
        
