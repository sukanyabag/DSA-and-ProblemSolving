/*
Given a list arr of N integers, print sums of all subsets in it.
Example 1:
Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function subsetSums() which takes
a list/vector and an integer N as an input parameter and return the list/vector of all the subset sums.

Expected Time Complexity: O(2N)
Expected Auxiliary Space: O(2N)

Constraints:
1 <= N <= 15
0 <= arr[i] <= 104

*/

//User function Template for Java//User function Template for Java
class Solution{
    ArrayList<Integer> subsetSums(ArrayList<Integer> arr, int N){
        // code here
        //init a new array to store subset sums
        ArrayList< Integer > sumOfSubsets = new ArrayList<>();
        
        helper(0,0,arr,N,sumOfSubsets);
        Collections.sort(sumOfSubsets);
        return sumOfSubsets;
    }
    
    static void helper(int idx, int sum, ArrayList<Integer> arr, int N, ArrayList<Integer> sumOfSubsets){
        //base case 
        if(idx == N){
            sumOfSubsets.add(sum);
            return;
        }
        
        //pick the element recursive call
        helper(idx+1, sum+arr.get(idx), arr, N, sumOfSubsets);
        
        //don't pick the element recursive call
        helper(idx+1, sum, arr, N, sumOfSubsets);
        
    }
}
