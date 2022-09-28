'''
LINK TO THE PROBLEM IN DESCRIPTION!
'''
'''
MEMOIZED CODE
Time Complexity: O(N*N)

Reason: There are N*(N+1) states therefore at max ‘N*(N+1)’ new problems will be solved.

Space Complexity: O(N*N) + O(N)

Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*(N+1)).
'''
def cutRod(price, n):
    # Write your code here.
    r,c = n,n+1
    dp = [[-1] * c for _ in range(r)]
    
    return self.memo(n-1,n,price,dp)

def memo(self,ind, n, price, dp):
    #base case 
    if(ind == 0):
        return n * price[0]
    
    if dp[ind][n] != -1:
        return dp[ind][n]

    notCut = 0 + self.memo(ind-1,n,price,dp)
    cut = float('-inf')
    rodLen = (ind+1)
    
    if(rodLen <= n):
        cut = price[ind] + self.memo(ind, n - rodLen, price,dp)
        
    dp[ind][n] = max(notCut,cut)
    
    return dp[ind][n]
