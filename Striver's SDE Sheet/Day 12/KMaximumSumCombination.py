'''
Given two equally sized 1-D arrays A, B containing N integers each.
A sum combination is made by adding one element from array A and another element of array B.
Return the maximum C valid sum combinations from all the possible sum combinations.

Problem Constraints
 1 <= N <= 105
 1 <= A[i] <= 103
 1 <= C <= N

Input Format
First argument is an one-dimensional integer array A of size N.
Second argument is an one-dimensional integer array B of size N.
Third argument is an integer C.

Output Format
Return a one-dimensional integer array of size C denoting the top C maximum sum combinations.

NOTE:
The returned array must be sorted in non-increasing order.

Example Input
Input 1:

 A = [3, 2]
 B = [1, 4]
 C = 2

Output 1:

 [7, 6]

Example Explanation
Explanation 1:

 7     (A : 3) + (B : 4)
 6     (A : 2) + (B : 4)

'''
import math
from queue import PriorityQueue
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        N = len(A)
        # Max heap.
        pq = PriorityQueue()
 
        # Insert all the possible
        # combinations in max heap.
        for i in range(0, N):
            for j in range(0, N):
                a = A[i] + B[j]
                pq.put((-a, a))
                
        # Pop first N elements from
        # max heap and display them.
        count = 0
        res = []
        while (count < C):
            x = (pq.get()[1])
            res.append(x)
            count += 1
        return res
