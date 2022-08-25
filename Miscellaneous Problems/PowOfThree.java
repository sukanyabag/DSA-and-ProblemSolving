//using math
class Solution {
    public boolean isPowerOfThree(int n) {
        //n is a power of three if and only if i is an integer
        //so check if 3 is raised to an integertype power 
        return (Math.log10(n) / Math.log10(3) % 1 == 0);
    }
}

//using a stfwd trick - Integer Limitations
/*
https://leetcode.com/problems/power-of-three/solution/
approach 4
*/
public class Solution {
    public boolean isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
}
