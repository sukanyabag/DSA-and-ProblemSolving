/* 
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Example 1:
Input: nums = [3,2,3]
Output: [3]

Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 
Follow up: Could you solve the problem in linear time and in O(1) space? 
The solution below has linear time (O(N)) and O(1) constant auxillary space.
Algorithm used - Enhanced Boyer Moore Voting Algorithm
*/

class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int num1= Integer.MIN_VALUE;
        int num2 = Integer.MIN_VALUE;
        int cnt1 = 0;
        int cnt2 = 0;
        
        int n = nums.length;
        
        for(int i = 0; i < n; i++){
            if(nums[i] == num1){
                cnt1 += 1;
            }
            else if(nums[i] == num2){
                cnt2 += 1;
            }
            else if(cnt1 == 0){
                num1 = nums[i];
                cnt1 = 1;
            }
            else if(cnt2 == 0){
                num2 = nums[i];
                cnt2 = 1;
            }
            else{
                cnt1--;
                cnt2--;
            }
        }
        
        ArrayList<Integer> res = new ArrayList<Integer>();
        cnt1 = 0;
        cnt2= 0;
        for(int i = 0; i < n; i++){
            if(nums[i] == num1){
                cnt1 += 1;
            }
            else if(nums[i] == num2){
                cnt2 += 1;
            }
        }
        
        if(cnt1>n/3){
            res.add(num1);
        }
        if(cnt2>n/3){
            res.add(num2);
        }
            
        return res;
        
    }
}
