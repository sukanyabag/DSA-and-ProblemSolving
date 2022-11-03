'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one 
share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''

class Solution:
    '''
    MEMOIZATION
    TC - O(N)
    SC - O(N)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        # states - buy, sell
        # buy = (i + 1)
        # sell = (i + 2) (since, 1 day will be needed for cooldown)
        dp = {} #key = (idx, bool(buy -> true, sell -> false)), val = max profit
        
        def dfs(i, canbuy):
            #base case
            if i >= len(prices):
                 return 0
        
            #visited
            if (i, canbuy) in dp:
                return dp[(i,canbuy)]
            
            # two states/choices - buy, not buy (sell)
                            
            cool = dfs(i+1, canbuy)
            
            if canbuy:
                buy = dfs(i+1, not canbuy) - prices[i]
                dp[(i, canbuy)] = max(buy, cool)
                
            else:
                sell = dfs(i+2, not canbuy) + prices[i]
                dp[(i, canbuy)] = max(sell, cool)
                
            return dp[(i, canbuy)]
        return dfs(0, True)
                
