/*  
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? Solution below takes linear time and space!
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(target - nums[i])){
                res[1] = i;
                res[0] =  map.get(target - nums[i]);
                
                return res;
            }
            
            map.put(nums[i],i);
        }
        
        return res;
    }
}
