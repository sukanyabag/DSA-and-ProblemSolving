/*  
Type 1 - Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. 
Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements. 
WITHOUT EXTRA SPACE👁️

Example 1:
Input: 
n = 4, arr1[] = [1 4 8 10] 
m = 5, arr2[] = [2 3 9]

Output: 
arr1[] = [1 2 3 4]
arr2[] = [8 9 10]

Explanation:
After merging the two non-decreasing arrays, we get, 1,2,3,4,8,9,10.
*/
import java.util.*;
class Day2{
    static void swap(int a,int b)
    {
        int temp=a;
        a=b;
        b=temp;
    }
   static void merge(int ar1[], int ar2[], int n, int m) {
  // code here 
    int gap =(int) Math.ceil((double)(n + m) / 2.0);
    while (gap > 0) {
      int i = 0;
      int j = gap;
      while (j < (n + m)) {
        if (j < n && ar1[i] > ar1[j]) {
          swap(ar1[i], ar1[j]);
      } else if (j >= n && i < n && ar1[i] > ar2[j - n]) {
          swap(ar1[i], ar2[j - n]);
      } else if (j >= n && i >= n && ar2[i - n] > ar2[j - n]) {
          swap(ar2[i - n], ar2[j - n]);
      }
      j++;
      i++;
    }
    if (gap == 1) {
      gap = 0;
    } else {
      gap =(int) Math.ceil((double) gap / 2.0);
    }
  }
}
  
 //Time complexity: O(logn), Space Complexity: O(1)
  
  

