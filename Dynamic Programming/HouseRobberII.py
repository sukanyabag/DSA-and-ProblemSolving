class Solution:
  
  #subarr = arr without first & last, get max of subarr, then pick which of first/last should be added to it
        
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
        
        
    def helper(self,nums):
        rob1, rob2 = 0,0
        
        for n in nums:
            newRob = max(rob1+n, rob2)
            #update rob1 and rob2
            rob1 = rob2
            rob2 = newRob
        return rob2
        
