/*
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
*/

class Pair{
    int first;
    int second;
    
    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}


class Solution {
    public void bfs(int r, int c, int[][] vis, char[][] grid){
        //init visited 
        vis[r][c] = 1;
        //number of row and col\
        int n = grid.length;
        int m = grid[0].length;
        
        //init queue
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(r,c));
        
        //loop over q to pop row, col
        while(!q.isEmpty()){
            int row = q.peek().first;
            int col = q.peek().second;
            q.remove();
            
            
          //traverse neighbors and mark them visited if land found
            for(int delrow = -1; delrow <= 1; delrow++){
                for(int delcol = -1; delcol <= 1; delcol++){
                      //not to check the diagonal elements
                    if((delrow == -1 && delcol == -1) || (delrow == -1 && delcol == 1) 
                       || (delrow == 1 && delcol == -1) || (delrow == 1 && delcol == 1)) continue;
                    
                    int nrow = row + delrow;
                    int ncol = col + delcol;
                    
                     if(nrow>=0 && nrow<n && ncol>=0 && ncol<m && grid[nrow][ncol]=='1' && vis[nrow][ncol]==0){
                        vis[nrow][ncol]=1;
                        q.add(new Pair (nrow,ncol));
                    }
                }
            }
        }
        
        
        
    }
    public int numIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int cnt=0;
        int[][] vis = new int[n][m];
        for(int row=0;row<n;row++){
            for(int col=0;col<m;col++){
                if(vis[row][col]==0 && grid[row][col]=='1'){
                    bfs(row,col,vis,grid);
                    cnt++;
                }
            }
        }
        return cnt;
        
    }
}
