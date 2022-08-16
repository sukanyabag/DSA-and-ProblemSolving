/* 
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
*/

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        //sort arr to have duplicates next to each other
        Arrays.sort(nums);
        
        //ds to store subsets
        List< List< Integer > > result = new ArrayList<>();
        
        //recursive call 
        findSubsets(0,nums,new ArrayList<>(),result);
        
        return result;
    }
    
    static void findSubsets(int idx, int[] nums, List<Integer> ds, List<List<Integer>> result){
        //add every subset 'ds' to the final list of lists 'result'
        result.add(new ArrayList<>(ds));
        
        //start checking from idx 0 to n-1
        for(int i=idx; i<nums.length; i++){
            
            //duplicates if found, simply ignore them and continue further
            if(i != idx && nums[i] == nums[i-1]) continue;
            
            //if it's the 1st time we are picking it, add it to ds
            ds.add(nums[i]);
            
            //now find the next subsets
            findSubsets(i+1,nums,ds,result);
            
            //remove the last elm from the ds after it is added as it should 
            //not be there in next recursive call
            ds.remove(ds.size() - 1);
            
        }
    }
}
