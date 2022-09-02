class Solution:
        
    def rob(self, nums: List[int]) -> int:
        #1st house and last house both cannot be robbed as they are circularly adjacent
        #to not take 1st house take all except 1 [1:]
        # to not take last take all except -1 [:-1]
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
        
        
    def helper(self,nums):
        rob1, rob2 = 0,0
        
        for n in nums:
            #adjacent houses cant be robbed
            #[rob1,rob2,n,n+1,....]
            #so if rob1, rob2 cannot be taken so rob1+n or rob2 and their max
            newRob = max(rob1+n, rob2)
            #update rob1 and rob2
            rob1 = rob2
            rob2 = newRob
        return rob2
        
