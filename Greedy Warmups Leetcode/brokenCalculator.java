/* 
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:
multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

Example 1:
Input: startValue = 2, target = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Constraints:

1 <= startValue, target <= 109
*/

class Solution {
    public int brokenCalc(int startValue, int target) {
        int minops = 0;
        
        while(target > startValue){
            //if target is not div by 2 (odd) increment it by 1
            if(target % 2 == 1){
                target++;
            }
            else{
                //greedily divide amap until our target becomes less then startValue.
                target/=2;
            }
            
            minops++;
        }
        
        //when target less than the startValue, while stops 
        //now add 1 to target to make it equal to startValue
        //so minops = minops + (startVal - target)
        //(since target and starval will always have diff of 1)
        return minops + (startValue - target);
    }
}
