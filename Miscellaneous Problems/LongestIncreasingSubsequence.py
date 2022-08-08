'''
Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order 
of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 
Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

BELOW SOLUTION USES DP WITH BINARY SEARCH APPROACH with O(n log(n)) time complexity
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        
        for elm in nums:
            #bisect_left() returns the idx in the sorted list,
            #where the element passed in argument can be placed 
            #so as to maintain the resultant sequence in sorted (increasing)order.
            idx = bisect_left(dp,elm)
            #entire array is traversed
            if idx == len(dp):
                dp.append(elm)
            #update dp[idx] with elm
            else:
                dp[idx] = elm
                
        #return longest increasing subsequence
        return len(dp)
        
