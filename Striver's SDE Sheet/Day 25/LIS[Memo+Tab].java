'''
'''

//MEMOIZATION - Time Complexity: O(N*N)
//Space Complexity: O(N*N) + O(N)-aux stack space
class Solution{
    public int getAns(int arr[], int n,  int ind, int prev_index,int[][] dp){
        // base condition
        if(ind == n)
            return 0;

        if(dp[ind][prev_index+1]!=-1)
            return dp[ind][prev_index+1];

        int notTake = 0 + getAns(arr,n,ind+1,prev_index,dp);

        int take = 0;

        if(prev_index == -1 || arr[ind] > arr[prev_index]){
            take = 1 + getAns(arr,n,ind+1,ind,dp);
        }

        return dp[ind][prev_index+1] = Math.max(notTake,take);
    }

    public int lengthOfLIS(int arr[]){
        int n = arr.length;
        int dp[][]=new int[n][n+1];
        for(int row[]: dp)
        Arrays.fill(row,-1);

        return getAns(arr,n,0,-1,dp);
    }
    
}


//TABULATION  - bottom up
//Time Complexity: O(N*N)
//Space Complexity: O(N*N)

class Solution {
    public int lengthOfLIS(int[] arr) {
        int n = arr.length;
        int dp[][]=new int[n+1][n+1];
    
        for(int i = n-1; i >= 0; i--){
            for(int prev_index = i-1; prev_index >= -1; prev_index--){

              int len = 0 + dp[i+1][prev_index + 1];

              if(prev_index == -1 || arr[i] > arr[prev_index]){
                  len = Math.max(len, 1 + dp[i+1][i+1]);        
              }

              dp[i][prev_index + 1] = len;

            }
        }

    return dp[0][0];
	}

}
