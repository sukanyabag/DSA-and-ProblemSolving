/* 
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
Return the total number of bad pairs in nums.
Example 1:
Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
*/
Logic - 
We do this in two different ways here:
First, instead of finding the number of pairs that are bad, we'll find the number of pairs that are not bad 
and subtract it from the total number of pairs.

Remember, for an array of size n, there are exactly n * (n - 1) / 2 unique pairs (i, j) where i < j. 
We get this from the sum of i from i = 1 to i = n.

Then, consider the equation, j - i = nums[j] - nums[i]. 
Given, two unique indices i, j on both sides of this equation
is disturbing. It'd be easier if we could consider them individually. 

So, let's rearrange the equation using basic algebra: nums[i] - i = nums[j] - j

total pairs - good pairs = bad pairs

res = 4*3 / 2 = 6

arr = [4.1,3,3]
map
key(nums[i]-i)  val(no of occurence)
4                 1
0                 2
1                 1



res = res - map.getOrDefault(4-0, 0) = 6 - 0 = 6
map.put(4, 0 + 1);
res = res - map.getOrDefault(1-1, 0) = 6 - 0 = 6
map.put(0, 0 + 1);
res = res - map.getOrDefault(3-2, 0) = 6 - 0 = 6
map.put(1, 0 + 1);
res = res - map.getOrDefault(3-3, 1) = 6 - 1 = 5
map.put(0, 1 + 1);

no of bad pairs = 5

pseudocode - 
1. init res = store total no of uniq pairs ( formula - (n*(n-1))/2 )
2. init a hashmap<int,int> with key as nums[i] - i and val as count of nums[i] - i
3. loop from i=0 to end of array(i<arr.length)
  3.1 for each i, subtract from result the occurence of nums[i]-i, if it exists otherwise 0
  3.2 insert into the map the new count of nums[i]-i if it repeats
4 return result 

Code - 

class Solution {
    public long countBadPairs(int[] nums) {
        long res = (nums.length * (nums.length - 1L)) / 2;
        
        HashMap<Integer,Integer> map = new HashMap<>();
        
        for(int i=0; i<nums.length; i++){
            int val = map.getOrDefault(nums[i]-i,0);
            res = res - val;
            map.put(nums[i]-i , val + 1);
        }
        
        return res;
    }
}
