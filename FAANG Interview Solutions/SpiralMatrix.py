'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

#Take the first row plus the spiral order of the rotated remaining matrix. 
def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
