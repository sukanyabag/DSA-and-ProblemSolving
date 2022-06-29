/*  
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
*/

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet<Integer>();
        Set<Integer> intersection = new HashSet<Integer>();
        
        for(int i : nums1){
            s1.add(i);
        }
        
        for(int j : nums2){
            if(s1.contains(j)){
                intersection.add(j);
            }
            
        }
        
        int[] ans = new int[intersection.size()];
        int i = 0;
        for(int k : intersection){
           ans[i++] = k; 
        }
        
        return ans;
    }
}
