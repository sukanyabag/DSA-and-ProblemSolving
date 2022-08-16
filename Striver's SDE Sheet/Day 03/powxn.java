/*  
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

TC - O(log n)
SC - O(1)
*/

class Solution {
    public double myPow(double x, int n) {
        double res = 1.0;
        //check overflow - store a duplicate copy of n i.e pown using to avoid overflow
        long pown = n;
        //Check if pown is a negative number, in that case, make it a positive number.
        if(pown < 0){
            pown = -1 * pown;
        }
        
        //main logic
        while(pown > 0){
            //if power is odd
            if(pown % 2 == 1){
                res = res * x;
                pown -= 1;
            }
            //if power is even
            else{
                x = x * x;
                pown /= 2;
            }
        }
        
        // if pow to be raised is -ve, ans will be 1/res, since 2^(-1) = 1/2
        if(n<0) res = (double)(1.0) / (double)(res);
        //else return res
        return res;
    }
}
