'''
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
 
Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Constraints:
1 <= nums.length <= 200
-106 <= nums[i] <= 106
All the elements of nums are unique.
At most 5 * 104 calls in total will be made to reset and shuffle.
'''

class Solution(object):
    def __init__(self, nums):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

