/*
Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K.
The task is to find the element that would be at the k’th position of the final sorted array.

Example 1:
Input:
arr1[] = {2, 3, 6, 7, 9}
arr2[] = {1, 4, 8, 10}
k = 5
Output:
6
Explanation:
The final sorted array would be -
1, 2, 3, 4, 6, 7, 8, 9, 10
The 5th element of this array is 6.

Your Task:  
You don't need to read input or print anything. 
Your task is to complete the function kthElement() which takes the arrays arr1[], arr2[], its size N and M respectively and an
integer K as inputs and returns the element at the Kth position.

Expected Time Complexity: O(Log(N) + Log(M))
Expected Auxiliary Space: O(Log (N))

Constraints:
1 <= N, M <= 106
1 <= arr1i, arr2i < INT_MAX
1 <= K <= N+M
*/

//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

//TIME COMPLEXITY - O(Log(min(m,n)))
//SPACE COMPLEXITY - O(1)

//User function Template for Java
class GFG {
    public long kthElement( int arr1[], int arr2[], int n, int m, int k) {
        //take the array with min length for binary search
        if(n > m){
            return kthElement(arr2,arr1,m,n,k);
        }
        
        //if k > size of larger arr, lower bound (low) should be atleast (k-sizeoflargerarr)
        int lo = Math.max(0, k-m);
        //if k < size of smaller arr, we only need to pick k as upper bound (high)
        int hi = Math.min(k,n);
        
        while(lo <= hi){
            int partition1 = (lo + hi) / 2;
            int partition2 = k - partition1;
            int l1 = partition1 == 0 ? Integer.MIN_VALUE : arr1[partition1 - 1];
            int l2 = partition2 == 0 ? Integer.MIN_VALUE : arr2[partition2 - 1];
            int r1 = partition1 == n ? Integer.MAX_VALUE : arr1[partition1];
            int r2 = partition2 == m ? Integer.MAX_VALUE : arr2[partition2];
            
            if(l1 <= r2 && l2 <= r1) return Math.max(l1,l2);
            
            
            else if (l1 > r2) {
                //move left
                hi = partition1 - 1;
            }
            
            else{
                //move right
                lo = partition1 + 1;
                
            }
            
        }
        
        return 1;
        
        
        
    }
}
