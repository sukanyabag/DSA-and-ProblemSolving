class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #calc rows and cols length
        rows = len(grid)
        cols = len(grid[0])
        
        #set to mark visited positions
        visited = set()
        
        
        def dfs(r,c):
            #base case
            '''
            Trick - since we need the perimeter, we only care about edges of islands
            so, whenever we hit a boundary condition, we return 1 instead of 0
            '''
            if r<0 or r >= rows or c<0 or c == cols or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            
            #add to visited
            visited.add((r,c))
            
            #calc perimeter
            peri = dfs(r,c+1) #right
            peri += dfs(r,c-1) #left
            peri += dfs(r-1,c) #up
            peri += dfs(r+1,c) #down
            
            
            return peri
        
        #run dfs on the entire grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r,c)
            
            
        
        
