'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the 
array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() #indices
        lptr = rptr = 0

        while rptr < len(nums):
            #make sure q is monotonically decreasing
            # by popping smaller values from q
            while q and nums[q[-1]] < nums[rptr]:
                q.pop()
            #now add larger val indices
            q.append(rptr)

            #remove leftmost unnecessary val if oob from curr window
            if lptr > q[0]:
                q.popleft()

            #edge case  - consider strict size k while appending sw max to res 
            #from starting window to ending window fashion
            #increment lptr by 1 for next window iteration, then rptr too
            if (rptr + 1) >= k:
                res.append(nums[q[0]])
                lptr += 1
            rptr += 1

        return res
