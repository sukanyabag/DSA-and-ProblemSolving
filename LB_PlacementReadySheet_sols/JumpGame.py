'''
Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. 
Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.
Note: Return -1 if you can't reach the end of the array.

Example 1:

Input:
N = 11 
arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
Output: 3 
Explanation: 
First jump from 1st element to 2nd 
element with value 3. Now, from here 
we jump to 5th element with value 9, 
and from here we will jump to last. 

Your task:
You don't need to read input or print anything. 
Your task is to complete function minJumps() which takes the array arr and it's size N as input parameters and returns the minimum number of jumps.
If not possible returns -1.

Expected Time Complexity: O(N)
Expected Space Complexity: O(1)

Constraints:
1 ≤ N ≤ 107
0 ≤ arri ≤ 107
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = n - 1
        counter = 0
        l = r = 0

        #base case - start and end indices are 0
        if n==1:
            return 0

        while r < end:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])

            l  =  r+1
            r = farthest
            counter += 1

        return counter
