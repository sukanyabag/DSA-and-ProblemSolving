/*
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
*/

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        //init list of lists to store answer
        List<List<Integer>> res = new ArrayList<>();
        
        //make recursive call on entire candidates array
        findComboSum(0,candidates,target,res,new ArrayList<>());
        
        return res;
    }
    
    
    private void findComboSum(int idx, int[] candidates, int target, List<List<Integer>> res,List<Integer> ds){
        //base case is to check all indexes have been recursed
        if(idx == candidates.length){
            //target 0 means we have got subaaray with sum of elements == target
            if(target == 0){
                res.add(new ArrayList<>(ds));
            }
            
            return;
        }
        
        //if any elm is less then target pick it and add it to ds
        if(candidates[idx] <= target){
            //add it to existing ds
            ds.add(candidates[idx]);
            
            //make recursive call by reducing target from element added 
            findComboSum(idx, candidates, target - candidates[idx], res, ds);
            
            //remove last element for next recursive calls
            ds.remove(ds.size() - 1);
        }
        
        //else simply don't pick the element 
        findComboSum(idx+1, candidates, target, res, ds);

        
    }
}
