/* 
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

Solve for an optimal solution - Binary Search which takes O(log(mxn)) time complexity which is better than O(mxn) in case of linear search)
Space must be O(1)
*/

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int numRows = matrix.length;
        int numCols = matrix[0].length;
        //1st idx
        int low = 0;
        //last idx
        int high = (numRows * numCols) - 1;
        //base case check
        if(numRows == 0) return false;
        
        while(low <= high){
            int mid = low + (high - low) / 2;
            //true case - 1 
            if(matrix[mid/numCols][mid%numCols] == target) return true;
            
            //bin srch pointer shift logics
            // if val at mid is greater than target val, then target is at left side of mid
            //so update high to mid-1
            if(matrix[mid/numCols][mid%numCols] > target){
                high = mid - 1;
            }
            
            // if val at mid is lower than target val, then target is at right side of mid
            //so update low to mid+1
            else{
                low = mid + 1;
            }
            
        }
        //if nothing satisfies inside while loop there's no target found return false
        return false;
    }
}

