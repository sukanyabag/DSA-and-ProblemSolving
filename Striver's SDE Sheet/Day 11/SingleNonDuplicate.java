/*
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105

TRICK - 
[mid^1] gives previous even idx if mid = odd.
[mid^1] gives next odd idx if mid = even.
So instead of odd even conditions, just binary search with condition nums[mid] == nums[mid^1].
*/
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int lo = 0;
        int hi = nums.length - 2;
        
        while(lo <= hi){
            int mid = lo + (hi - lo) / 2;
            if(nums[mid] == nums[mid^1]){
                lo = mid + 1;
            }
            else{
                hi = mid - 1;
            }
        }
        
        return nums[lo];
    }
}
