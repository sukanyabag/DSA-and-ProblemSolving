'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Time: O(Nlogk)
Space: O(N)
'''
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        # freq dict
        freq_dict = {}
        for num in nums:
	        if num in freq_dict:
		        freq_dict[num] += 1
	        else:
		        freq_dict[num] = 1

        # insert k items into heap O(nlog(k))
        minheap = []
        for key in freq_dict: # O(N)
	        heappush(minheap, (freq_dict[key], key)) # freq, item - O(log(k))
	        if len(minheap) > k:
		        heappop(minheap)

        res = []
        while minheap: # O(k)
	        freq, elem = heappop(minheap) # O(logk)
	        res.append(elem)
        return res
