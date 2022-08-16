/* 
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, 
if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, 
the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]
*/


class Solution {
    public void nextPermutation(int[] nums) {
        //base case 
        if(nums == null || nums.length <= 1) return;
        //2nd last index - i and last index - (i+1)
        int i  = nums.length - 2;
        //as long as sequence is increasing from right to left, decrement i
        while(i>=0 && nums[i+1] <= nums[i]){
            i--;
            
        }
        //as soon as sequence starts decreasing at an index i, search for it's      
        //immediate increasing index j by traversing from end of the array (nums.length - 1)
        if (i>=0){
            //j pointer which starts at end of arr to search for index 
           //just greater than i (decrements until val > nums[i] is reached)
            int j = nums.length - 1;
            while(nums[j] <= nums[i]){
                j--;
            }
            //while stops when val > nums[i] is reached by j pointer
            //now i and j will be swapped
            swap(nums,i,j);
                
        }
        //all remaining from right will be reversed (to sort them in ascending ord) to get the next smallest lex perm
        reverse(nums, i+1);  
    }
    
    public void reverse(int[] nums, int start){
        int i = start, j = nums.length - 1;
        while(i<j){
            swap(nums, i, j);
            i++;
            j--;
        }
    }
    
    public void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
