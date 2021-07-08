/* 
Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
Example 1:

Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.

Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000

*/
class Solution {
    public boolean canBeIncreasing(int[] nums) {
        boolean isIncreasing = true;
        int n = nums.length;
        for(int i=0;i<n-1;i++){
            
            if(nums[i] >= nums[i+1]){
                if(!isIncreasing) return false;
                isIncreasing = false;
                if(i == 0 || i == n-2) continue;
                else if(nums[i+1] > nums[i-1] || nums[i+2] > nums[i]) continue;
                else return false;
                
            }
        }
        return true;
        
    }
}
