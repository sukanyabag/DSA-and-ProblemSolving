'''
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. 
The score of the team is the sum of scores of all the players in the team.
However, the basketball team is not allowed to have conflicts. 
A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.
Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, 
return the highest overall score of all possible basketball teams.

Example 1:
Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.

Example 2:
Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.

Constraints:
1 <= scores.length, ages.length <= 1000
scores.length == ages.length
1 <= scores[i] <= 106
1 <= ages[i] <= 1000
'''
'''
EXPLANATION - THIS PROBLEM IS VARIATION OF MSIS
The idea is to sort array of tuples (age, score) by age, then we can eliminate the age factor because as long as we choose 
elements at index i and j so that i > j then the age inside tuples[i] >= the age inside tuple[j], and we will not have conflicts.

For example:
[1,5,3,10,15]
[1,3,2,4,5]

The sorted tuples is:
[(1, 1), (2, 3), (3, 5), (4, 10), (5, 15)]
Now this problem boils down to Find the maximum sum increasing subsequence (MSIS) of scores array [1, 3, 5, 10, 15]
'''

#TABULATED CODE
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        AgeScoretuple = sorted(zip(ages,scores))
        
        n = len(AgeScoretuple) 
        
        dp = [0] * n
        
        for i in range(n):
            dp[i] = AgeScoretuple[i][1]
            
            for j in range(i):
                if(AgeScoretuple[i][1] >= AgeScoretuple[j][1]):
                    dp[i] = max(dp[i], dp[j] + AgeScoretuple[i][1])
                    
        return max(dp)
