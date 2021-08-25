'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false

Constraints:
1 <= num <= 2^31 - 1
'''

#newton's method
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        
        while r*r > num:
            
            r = (r + num/r) // 2
            
        return r*r == num
        
        
 #binary search
def BinarySearch(self, num):
        left = 0
        right = num
        
        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False
