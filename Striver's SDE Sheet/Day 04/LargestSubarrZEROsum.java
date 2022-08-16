/*  
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.
Example 1:
Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, 
where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
-1000 <= A[i] <= 1000, for each valid i
*/

class GfG
{
    int maxLen(int arr[], int n)
    {
        // Your code here
        // hashmap<int key (stores prefix sum), int val (idx of prefix sum)>
        HashMap<Integer,Integer> h = new HashMap<Integer,Integer>();
        //calculates longest sequence with 0 sum
        int maxseq = 0;
        //stores current sum
        int sum = 0;
        
        for(int i=0; i < n; i++){
            //find subarr sums
            sum += arr[i];
            
            //if at any idx sum is found to be 0, maxseq = (ith + 1)
            //ex - (1,-1) = 1-1 = 0 -> maxseq = 1+1 = 2
            if(sum == 0){
                maxseq = i + 1;
            }
          
            // if sum != 0
            else{
                //if sum does exist in the hashmap at any key
                if(h.get(sum) != null){
                    //get the idx of hashmap where that prefx sum exist
                    // subtract curr idx where you are from that hashmap idx to get length of seq
                    // compare it with maxseq so far, update  with maximum of the two
                    maxseq = Math.max(maxseq, i - h.get(sum));
                }
                
                //if sum does not appear before in hashmap's key
                else{
                    //put the prefix sum and its idx in the hashmap
                    h.put(sum,i);
                }
            }
        }
        //in the end return max sequence length
        return maxseq;
    }
}
