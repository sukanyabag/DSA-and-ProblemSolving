/*  
Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing 
and one number 'B' occurs twice in array. Find these two numbers.

Example 1:
Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and 
smallest positive missing number is 1.

Your Task:
You don't need to read input or print anything. 
Your task is to complete the function findTwoElement() which takes the array of integers arr 
and n as parameters and returns an array of integers of size 2 denoting the answer ( The first index contains B and second index contains A.)

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ N
*/

class Solve {
    int[] findTwoElement(int arr[], int n) {
        // code here
        int S = (n * (n+1) ) /2;
        int P = (n * (n+1) *(2*n+1) )/6;
        long missingNumber=0, repeating=0;
        
        int[] result = new int[2];
        
        for(int i=0;i<n; i++){
            S -= (int)arr[i];
            P -= (int)arr[i]*(int)arr[i];
        }
     
        missingNumber = (S + P/S)/2;

        repeating = missingNumber - S;
        
        result[0] = (int)repeating;
        result[1] = (int)missingNumber;

        return result;
    }
}
