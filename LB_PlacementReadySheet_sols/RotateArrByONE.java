/* 
Given an array, rotate the array by one position in clock-wise direction.
Example 1:
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4

our Task:  
You don't need to read input or print anything. 
Your task is to complete the function rotate() which takes the array A[] and its size N as inputs and modify the array.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1<=N<=105
0<=a[i]<=105
*/

//User function Template for Java

class Compute {
    
    public void rotate(int arr[], int n)
    {
        //Store last element in a variable
        int m = arr[arr.length - 1];
        int i;
        for (i = arr.length - 1; i > 0; i--){
            arr[i] = arr[i-1];
        
        }
        arr[0] = m;
    }
}

//Python3
/* 
def rotate( arr, n):
   x = arr[n-1]
   for i in range(n-1,0,-1):
       arr[i] = arr[i-1]
   arr[0] = x
   return arr

*/
