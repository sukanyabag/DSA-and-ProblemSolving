/*
You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of \
the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5
Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
 
Constraints:
1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.
*/

class Solution{
    public boolean isPossible(int[] nums) { 
        // left map represents how many numbers left to form intervals
        HashMap<Integer, Integer> left = new HashMap<>();
        // end map keeps track of the actual ends in those intervals
        HashMap<Integer, Integer> end = new HashMap<>();
        
        for (int num: nums) left.put(num, left.getOrDefault(num, 0) + 1);
        for (int num: nums) {
            // continue, if no num has been left

            if (left.get(num) <= 0) continue;
            
            //else use num by 1, reduce its count by 1 too
            left.put(num, left.get(num) - 1);
            
            //to find if there is any previous interval...
            //if there is, append this num to it.
            //just greedily place num in an existing subsequence if possible
            if (end.containsKey(num-1) && end.get(num-1) > 0) {
                end.put(num-1, end.get(num-1) - 1);
                end.put(num, end.getOrDefault(num, 0) + 1);
                continue;
            }
            
            // to find if there is any possibility to form an interval based on the upcoming two elements after num: if there is, 
            //then use these 3 num and update their end.

            if (left.containsKey(num+1) && left.get(num+1) > 0 && left.containsKey(num+2) && left.get(num+2) > 0){
                left.put(num+1, left.get(num+1) - 1);
                left.put(num+2, left.get(num+2) - 1);
                end.put(num+2, end.getOrDefault(num+2, 0) + 1);
                continue;
            }
            
            // cannot find a space to place num? game over!
            return false;
        }
        
        return true;
    }
}
    

