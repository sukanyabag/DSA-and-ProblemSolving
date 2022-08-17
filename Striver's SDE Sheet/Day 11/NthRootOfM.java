/*
Problem Statement: Given two numbers N and M, find the Nth root of M.

The nth root of a number M is defined as a number X when raised to the power N equals M.

Example 1:

Input: N=3 M=27

Output: 3

Explanation: The cube root of 27 is 3.

Note - 
1. N is a real number.
2. Print answer upto 6 decimal places.
*/

class GFG {
    private static double multiply(double number, int n) {
        double ans = 1.0;
        for(int i = 1;i<=n;i++) {
            ans = ans * number;
        }
        return ans; 
    }
    private static void getNthRoot(int n, int m) {
        double low = 1;
        double high = m;
        double eps = 1e-6; 
        
        while((high - low) > eps) {
            double mid = (low + high) / 2.0; 
            if(multiply(mid, n) < m) {
                low = mid; 
            }
            else {
                high = mid; 
            }
        }
    }
