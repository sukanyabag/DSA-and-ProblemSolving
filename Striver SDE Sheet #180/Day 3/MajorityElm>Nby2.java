/* 
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space? Solution below takes TC - O(N) ans SC - O(1)
*/

class Solution {
    public int majorityElement(int[] nums) {
        int cnt = 0;
        int candidate = 0;
        
        //Moore's Voting Algorithm         
        for(int i : nums){
            if(cnt == 0){
                candidate = i;
            }
            if(i == candidate) cnt++;
            else cnt--;
        }
        
        return candidate;
    }
}
