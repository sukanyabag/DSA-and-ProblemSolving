/*
Problem Statement: Given a row-wise sorted matrix of size r*c, where r is no. of rows and c is no. of columns, find the median in the given matrix.

Assume – r*c is odd

Examples:

Example 1:
Input: 
r = 3 , c = 3
1 4 9 
2 5 6
3 8 7
Output: Median = 5
Explanation: If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9
So, median = 5

Example 2:
Input: 
r = 3 , c = 3
1 3 8
2 3 4
1 2 5
Output: Median = 3
Explanation: If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 7 8
So, median = 3
*/
public class MedianOfMatrix {
    public static int findMedian(ArrayList<ArrayList<Integer>> matrix) {
        int low = 1, high = (int)1e9;
        int n = matrix.size();
        int m = matrix.get(0).size();
        while (low <= high) {
            int mid = (low + high) / 2;
            int count = 0;
            for (int i = 0; i < n; i++) {
                count += countSmallerThanMid(matrix.get(i), mid);
            }

            if (count <= (n * m) / 2) 
                low = mid + 1;
            else
                high = mid - 1;
        }

        return low;
    }

    public static int countSmallerThanMid(ArrayList<Integer> row, int mid) {
        int low = 0, high = row.size() - 1;
        while (low <= high) {
            int md = (low + high) / 2;
            if (row.get(md) <= mid)
                low = md + 1;
            else
                high = md - 1;
        }

        return low;
    }

    public static void main(String[] args) {
        
    }
}
