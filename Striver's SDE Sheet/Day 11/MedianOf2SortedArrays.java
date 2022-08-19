/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
*/

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        
        //make sure binary search is being done on smaller sized array
        if(m > n){
            return findMedianSortedArrays(nums2,nums1);
        }
        
        //pointers
        int lo = 0;
        int hi = m;
        
        //calc med pos
        int medPos = ((m + n) + 1) / 2;
        
        //binary search 
        while(lo <= hi){
            int partition1 = (lo + hi) / 2;
            int partition2 = medPos - partition1;
            
            int l1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
            int l2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];
            
            int r1 = (partition1 == m) ? Integer.MAX_VALUE : nums1[partition1];
            int r2 = (partition2 == n) ? Integer.MAX_VALUE : nums2[partition2];
            
            //partitioning is valid, so compute median
            if(l1 <= r2 && l2 <= r1){
                if((m + n) % 2 != 0) return Math.max(l1,l2);
                else return (Math.max(l1,l2) + Math.min(r1,r2)) / 2.0;
            }
            
            //partitioning not valid, so shift ranges
            else if(l1 > r2) hi = partition1 - 1;
            else lo = partition1 + 1; 
        }
        
        return 0.0;
        
    }
}
