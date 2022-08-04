/*
There is a special square room with mirrors on each of the four walls. Except for the southwest corner,
there are receptors on each of the remaining corners, numbered 0, 1, and 2.
The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.

Example 1:
Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Constraints:
1 <= q <= p <= 1000

*/

/* 
very bull problem, but still - 

extenstion * p = reflection * q

where, 
extension = number of room extension + 1
reflection = number of reflection + 1

if extension = EVEN and reflection = ODD -> ray always reaches receptor 0
if extension = ODD and reflection = EVEN -> ray always reaches receptor 2
if extension = ODD and reflection = ODD -> ray always reaches receptor 1

Any other case is practically not possible.

*/

class Solution {
    public int mirrorReflection(int p, int q) {
        int extension = q;
        int reflection = p;
        
        while(extension % 2 == 0 && reflection % 2 == 0){
            extension /= 2;
            reflection /= 2;
        }
        
        if(extension % 2 == 0 && reflection % 2 != 0) return 0;
        if(extension % 2 != 0 && reflection % 2 == 0) return 2;
        if(extension % 2 != 0 && reflection % 2 != 0) return 1;
        
        return -1;
        
    }
}
