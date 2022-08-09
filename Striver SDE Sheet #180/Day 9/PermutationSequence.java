/*
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Example 1:
Input: n = 3, k = 3
Output: "213"

Constraints:
1 <= n <= 9
1 <= k <= n!
*/

class Solution {
    public String getPermutation(int n, int k) {
        int fact = 1;
        List<Integer> nums = new ArrayList<>();
        for(int i=1; i < n; i++){
            fact *= i;
            nums.add(i);
        }
        
        nums.add(n);
        String res = "";
        k = k - 1;
        
        while(true){
            res =  res + nums.get(k/fact);
            nums.remove(k/fact);
            if(nums.size() == 0) break;
            
            k = k % fact;
            fact = fact / nums.size();
        }
        
        return res;   
    }
}
