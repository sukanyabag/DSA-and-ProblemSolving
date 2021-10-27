'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Constraints:
1 <= n <= 45
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        #simple fibonacci sequence gives us the result
        #steps -                  1    2     3        4       5       6        7 ...........
        #ways(fibonacci seq) -    1  (1+1=2) (2+1=3) (3+2=5) (5+3=8) (8+5=13) (13+8=21).....
        if n <= 2:
            return n
        
        prev1 = 1
        prev2 = 2
        
        for i in range(2,n):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return current
        
