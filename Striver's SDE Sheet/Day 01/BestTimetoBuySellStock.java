/*  
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
*/

class Solution {
    public int maxProfit(int[] prices) {
        int currMin = prices.length > 0 ? prices[0] : 0;
        int profit = 0;
        
        for(int i=0; i < prices.length; i++ ){
            currMin = Math.min(prices[i], currMin);
            profit = Math.max(prices[i] - currMin, profit);
        }
        
        return profit;
    }
}
