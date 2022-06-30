/*  
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

*/

class Solution {
    public void setZeroes(int[][] matrix) {
        boolean isCol = false;
        int rows = matrix.length;
        int columns = matrix[0].length;
        
         //STEP 1
        //1st traverse the matrix linearly
        for(int i=0; i< rows; i++){
            //if element at ith row and 1st col is 0, set isCol = true
            if(matrix[i][0] == 0){
                isCol = true;
            }
        
            
            //STEP 2
            for(int j=1; j<columns;j++){
                //if elm at ith row and jth col is 0
                if(matrix[i][j] == 0){
                    //set leftmost elm on that row to 0
                    matrix[i][0] = 0;
                    //set topmost elm on that col to 0
                    matrix[0][j] = 0;
                }
            }
            
        }
            //STEP 3
            //traversing the matrix backwards since dummy R and C needs to be reserved
            for(int i = rows-1; i>=0; i--){
                for(int j = columns-1; j>=1; j--){
                    //if leftmost or topmost is 0, update elm in ith row & jth col to 0
                    if(matrix[i][0] ==0 || matrix[0][j] == 0){
                        matrix[i][j] = 0;
                    }
                }
                
            //STEP 4 -  now we can update dummies
            //so, check if any elemnt in the 1st column is 0 i.e. isCol == true
            //then set col[0] to 0
                if (isCol)
                    matrix[i][0] = 0;
            }
               
        }
        
    }
