/* 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
*/

class Solution {
    public int longestConsecutive(int[] nums) {
        //init hashset
        Set<Integer> hashSet = new HashSet<Integer>();
        
        //copy all elms to hashset
        for(int num : nums){
            hashSet.add(num);
        }
        
        //computes max of all consecutive sequences
        int longestStreak = 0;
        
        //linearly iterate for num in nums array
        for(int num : nums){
            //if hashset doesn't contain num - 1 proceed
            if(!hashSet.contains(num - 1)){
                //set currNum as num
                int currNum = num;
                // set currStreak as 1 as this is 1st iteration
                int currStreak = 1;
                
                //keep on running while loop till we are getting a sequence
                while (hashSet.contains(currNum+1)){
                //increment currNum by 1 
                currNum += 1;
                //increment currStreak by 1 
                currStreak += 1;   
             }
             
            //of all sequences found, compare and set the max seq length to longestStreak 
            longestStreak = Math.max(longestStreak, currStreak);
            
        }
        
    }
        
        return longestStreak;
}
    
}
        
