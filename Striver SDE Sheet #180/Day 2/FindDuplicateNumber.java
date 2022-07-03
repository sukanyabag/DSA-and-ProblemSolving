/*  
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Solution is optimal (solved by linked list cycle method) and takes O(N)/ linear time.
*/

class Solution {
    public int findDuplicate(int[] nums) {
        //step1 - start slow and fast pointers at 1st idx 
        //and move slow and fast by 1 and 2 pos resp. (check do while loop)
        //as soon as slow=fast (collision) while breaks and then set fast to 1st idx
        int slow = nums[0];
        int fast = nums[0];
        
        do{
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while(slow != fast);
        
        fast = nums[0];
        
        //step2
        //now move slow and fast each by one pos (loop until they collide again)
        while(slow!=fast){
            slow = nums[slow];
            fast = nums[fast];
        }
        
        //step 3 - as soon as slow and fast collide, step 2's while breaks
        //breakpoint is repeating val
        //return slow (duplicate val)
        return slow;
    }
}
