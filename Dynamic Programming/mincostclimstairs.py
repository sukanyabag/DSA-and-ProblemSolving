class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #add an extra index for goal with 0 cost
        cost.append(0)
        
        #start from 3rd last val and then do bottom up
        #we do this because we cannot take jump at last or 2nd last(cannot take 2 jumps)
        for i in range(len(cost) - 3, -1, -1):
            #[i+1] for 1 jump and i+2 for double jump
            #take min of single and double jump
            #add to cost at i
            
            cost[i] += min(cost[i+1], cost[i+2])
            
            
        #since atleast 2 stairs will be there, we can return min of 1st and 2nd costs
        return min(cost[0],cost[1])
        
