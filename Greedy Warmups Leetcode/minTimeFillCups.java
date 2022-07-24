/* 
You have a water dispenser that can dispense cold, warm, and hot water. 
Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.
You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2]
denote the number of cold, warm, and hot water cups you need to fill respectively. 
Return the minimum number of seconds needed to fill up all the cups.

Example 1:
Input: amount = [1,4,2]
Output: 4
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup and a warm cup.
Second 2: Fill up a warm cup and a hot cup.
Second 3: Fill up a warm cup and a hot cup.
Second 4: Fill up a warm cup.
It can be proven that 4 is the minimum number of seconds needed.

Constraints:
amount.length == 3
0 <= amount[i] <= 100
*/

class Solution {
    public int fillCups(int[] amount) {
        Arrays.sort(amount);
        int sum = 0;
        int maxcups = 0;
        
        for(int i : amount){
            maxcups = Math.max(i,maxcups);
            sum += i;
        }
        
        return Math.max(maxcups,(sum+1)/2);
    }
}
