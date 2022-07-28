'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the 
array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= target:
                target  = i
                
        return target == 0 
        
        
'''
Intuition - GREEDY APPROACH (O(N) time)
1. init target to end of list

2. back traverse the list

3. check if this jump from ith idx to jump length is greater than or equal to target or not
(where, i -> idx, nums[i] -> length of current jump)

4. if the jump len (i + nums[i]) is greater than or equal to target, we can jump to target

5. if we are able to reach target, we shift target closer to us and do step 3 again

6. if everytime we can reach target, target shifts closer to start

7. At the end finally target becomes 0 if all jumps are valid. If it doesn't it simply means we cannot reach the target at a certain idx (any of the jump len is invalid).
'''
