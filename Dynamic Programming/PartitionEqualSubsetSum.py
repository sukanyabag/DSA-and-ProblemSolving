class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #check edge case 
        if sum(nums) % 2 == 1:
            return False
        
        dp = set()
        
        # since in the beginning sum will be 0, so add 0 to the set
        dp.add(0)
        
        target = sum(nums) // 2
        
        for i in range(len(nums)-1,-1,-1):
            nxtdp = set()
            for t in dp:
                if(t + nums[i] == target):
                    return True
                
                #either add t or add sum of t with curr subset sums
                nxtdp.add(t)
                nxtdp.add(t + nums[i])
                
            dp = nxtdp
            
        return True if target in dp else False
