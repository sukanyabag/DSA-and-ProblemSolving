/*
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost 
row or leftmost column and going in the bottom-right direction until reaching the matrix's end.
For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
*/

/**
-------------------------EXPLANATION AND TC-SC ANALYSIS -------------------------
According to hint #3 -> All cells in the same diagonal (i,j) have the same difference.
So we can get the diagonal of a cell using the difference (i-j).
1. So we simply get the diagonals.
2. Then for every diagonal we get, we push its resp elements to a priority queue.
3. Next, we sort them (priority queue in Java pops out elements in their natural order by default).
4. After priority queue gets us the sorted order of diagonal elements, all we need to do is
update matrix[i][j] with sorted order of diagonal elements as popped by the priority queue.

Time-Space Analysis - 
For enqueing and dequeing methods, the time complexity is O(log(k)).
The nested loops give us the O(mn), to which we sum the complexity of the loop
where we sort: that one is (m+n)klogk.
(where, total diagonals is (m+n) and each of them is log k, so that gives us (m+n)klogk.)

So overall -> TC is O(mnlogk), with k = min(m,n).
((m+n)klogk becomes mnlogk, because (m+n)*min(m,n) ~ mn.)
--------------------------------END-------------------------------------------------------
**/

class Solution {
    public int[][] diagonalSort(int[][] mat) {
        //compute rows and cols
        int r = mat.length;
        int c = mat[0].length;
        
        //init hashmap that store diagonal position as key and element as value
        //values should be stored in a priority queue to pop them out in sorted manner later
        HashMap< Integer, PriorityQueue<Integer> > map = new HashMap<>();
        
        //loop over and insert idx and elements of respective diagonals
        //putIfAbsent -> used to map the specified key with its val, if no such key exists
        //otherwise if that idx(key) exists, we just put element present at that pos to the pq
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                map.putIfAbsent(i-j, new PriorityQueue<>());
                map.get(i-j).add(mat[i][j]);
            }
        }
        
        //this loop pops elem from pq to get us the sorted order of diagonal elements
        //then we update mat[i][j] with sorted order of diagonal 
        for (int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                int sortedDiag = map.get(i-j).poll();
                mat[i][j] = sortedDiag;
            }
        }
        
        return mat;
        
        
    }
}
------------------------------------------------------------------------check description for follow up-----------------------------------------------------------------
