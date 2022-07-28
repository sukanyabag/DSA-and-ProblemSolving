'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside 
the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Constraints:
-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        #check if number is negative
        isneg = x < 0
        
        #take absolute value of x, convert it to string and reverse it, typecast it back to int
        reverse_x = int(str(abs(x))[::-1])
        
        #consider 32 bit range check as asked in question
        if reverse_x >= -2**31 and reverse_x <= 2**31 - 1:
            #if negative return negative of reverse_x
            if isneg: 
                return -reverse_x
              
             #else return reverse_x
            return reverse_x
        
        # overflow condition -  If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
        else:
            return 0
    

