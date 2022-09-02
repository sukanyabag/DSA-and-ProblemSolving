class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
    
'''
basic idea -> for arrays with pos as well as neg integers, take a max-min pair
idea is to store the product if we take an elem in subarr, and also if we not take 

for ex - [-1,-2,-3]
take -1 -> -1x-2 = 2
not take -1 -> -2 = -2
therefore, max,min = 2,-2

for -3, we take prev computed max min 
take -2 -> -3 x -2 = 6
take 2 -> -3 x 2 = -6
therefore new max,min = 6,-6 

...and so on until we get max subarray prod
'''
