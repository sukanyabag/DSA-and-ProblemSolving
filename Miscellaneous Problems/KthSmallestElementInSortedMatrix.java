/*
For example, given a matrix and k = 8,
[[ 1, 5, 9],
[10, 11, 13],
[12, 13, 15]],

low = matrix[0][0] = 1, high = matrix[2][2] = 15, mid = 8, count is element number of set {1, 5} = 2, count < k, let low = mid + 1 = 9;

low = 9, high = 15, mid = 12, count is element number of set {1, 5, 9, 10, 11, 12} = 6, count < k, let low = mid + 1 = 13;

low = 13, high = 15, mid = 14, count is element number of set {1, 5, 9, 10, 11, 12, 13, 13} = 8, count = k, but the element we need is 13, 
not the mid(14), so let high = mid = 14 to narrow the search gap.

low = 13, high = 14, mid = 13, count = 8, count = k, let high = mid = 13,

low = 13, high = 13, low and high are meet, now return low.

Note - using (low < high) in while loop rather than using (low <= high) to avoid stay in the loop. It takes log(n * n) times to find mid,
and using (2n) times to get count in each loop, so exact time complexity is O((2n) log (n * n)). 
The matrix is n x n, So the approx time complexity is O(n log (n^2)).
*/

class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int m = matrix.length;
        int low = matrix[0][0], high = matrix[m - 1][m - 1];
        while (low < high) {
            int mid = (high - low) / 2 + low;
            int count = 0; 
            int j = m - 1;
            for (int i = 0; i < m; i++) {
                while (j >= 0 && matrix[i][j] > mid)
                    j--;
                count += j + 1;
            }
            if (count < k)
                low = mid + 1;
            else
                high = mid;
        }
        return low;
    }
}

*/
