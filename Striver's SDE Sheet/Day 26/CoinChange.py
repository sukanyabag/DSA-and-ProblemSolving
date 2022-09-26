'''
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''
#TABULATED BOTTOMUP DP APPROACH
#TC - O(AMOUNT * LEN(COINS))
#SC - O(AMOUNT)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        
        #base
        dp[0] = 0
        
        for amt in range(1,amount+1):
            for coin in coins:
                if (amt-coin) >= 0:
                    #coin=4, amt = 7, 
                    #then dp[7] = 1(1 denom of coin 4) + dp[amt-coin] =  1 + dp[3] = 1+1 = 2
                    dp[amt] = min(dp[amt], 1 + dp[amt-coin])
                    
        return dp[amount] if dp[amount] != amount+1 else -1
            
