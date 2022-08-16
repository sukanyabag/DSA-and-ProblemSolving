/* 
Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

Example 1:
Input: nums = [1,3,2,3,1]
Output: 2

Constraints:
1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1
*/

class Solution {
    public int reversePairs(int[] nums) {
        
        return mergeSort(nums, 0, nums.length - 1);
        
    }
    
    public int mergeSort(int[] nums, int low, int high){
        // base case check
        if(low >= high) return 0;
        
        //merge sort logic 
        int mid =  low + (high - low) /2;
        //left half
        int inversions = mergeSort(nums, low, mid);
        //right half
        inversions += mergeSort(nums, mid+1, high);
        //whole
        inversions += merge(nums, low, mid, high);
        
        return inversions;
        
    }
    
    public int merge(int[] nums, int low, int mid, int high){
        int count = 0;
        int j = mid + 1;
        
        for(int i = low; i <= mid; i++){
            //if condition satisfied move j further
            while(j <= high && nums[i] > (2 * (long) nums[j])){
                j++;
            }
            //if condition does not satisfy count will not be incremented
            //(count += (mid+1) - (mid+1)) which is count += 0
            count += (j - (mid+1));
        }
        
        ArrayList<Integer> tmp = new ArrayList<>();
        int L = low;
        int R = mid + 1;
        
        while(L <= mid && R <= high){
            if(nums[L] <= nums[R]){
                tmp.add(nums[L++]);
            }
            else{
                tmp.add(nums[R++]);
            }
        }
        
        //if anything left at L copy to L
        while(L <= mid){
            tmp.add(nums[L++]);
        }
        //if anything left at R copy to R
        while(R <= high){
            tmp.add(nums[R++]);
        }
        
        //overwrite the original arr with temporary arr
        for(int i = low; i <= high; i++){
            nums[i] = tmp.get(i - low);
        }
        
        return count;
        
        
    }
}
