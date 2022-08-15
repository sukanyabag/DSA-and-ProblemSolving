/*
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
*/

Approach #1 - RECURSION Time Complexity:  N! x N , Space Complexity:  O(N)
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        //stores perms
        List<List<Integer>> res = new ArrayList<>();
        
        //stores perms while recursing
        List<Integer> ds = new ArrayList<>();
        
        //marks which elm is taken
        boolean markvis[] = new boolean[nums.length];
        
        //call recr func on entire nums array
        recurPermute(nums,ds,res,markvis);
        
        //return permutations
        return res;
    }
    
    
    private void recurPermute(int[] nums, List<Integer> ds, List<List<Integer>> res, boolean[] markvis){
        //base case check
        if(ds.size() == nums.length){
            res.add(new ArrayList<>(ds));
            return;
        }
        
        //iterate(i) from 0 to n(nums.length)
        for(int i = 0; i < nums.length; i++){
            //if elm not marked as visited yet, pick it
            if(!markvis[i]){
                //mark it as picked
                markvis[i] = true;
                //add it to the ds
                ds.add(nums[i]);
                //make the recursive call
                recurPermute(nums,ds,res,markvis);
                //backtrack and remove last elm added
                ds.remove(ds.size() - 1);
                //since elm removed unmark it 
                markvis[i] = false;  
            }
        }
    }
    
}



Approach #2 - BACKTRACKING AND SWAPPING Time Complexity:  N! x N , Space Complexity:  O(1)
class Solution {
    private void recurPermute(int index, int[] nums, List < List < Integer >> ans) {
        if (index == nums.length) {
            // copy the ds to ans
            List < Integer > ds = new ArrayList < > ();
            for (int i = 0; i < nums.length; i++) {
                ds.add(nums[i]);
            }
            ans.add(new ArrayList < > (ds));
            return;
        }
        for (int i = index; i < nums.length; i++) {
            //swap from i to n-1
            swap(i, index, nums);
            //make recursive calls for next indexes
            recurPermute(index + 1, nums, ans);
            //while baktracking re-swap
            swap(i, index, nums);
        }
    }
  
    //this snippet is a helper swap func
    private void swap(int i, int j, int[] nums) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
  
    //main
    public List < List < Integer >> permute(int[] nums) {
        List < List < Integer >> ans = new ArrayList < > ();
        recurPermute(0, nums, ans);
        return ans;
    }
};
