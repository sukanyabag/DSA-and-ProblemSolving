
#BRUTE - SORTING
#TC - O(NlogN)
#SC - O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
      
      
#BETTER - MAX HEAP
#TC - O(N + k log N) => O(k log N)
# build max heap - O(N)
# take max element out - O(log N)
# do this k times to take out kth largest elm - O(k log N)
# TC => O(N + k log N) => O(k log N)
#SC - O(N)

'''
NOTE - We use heapq class to implement Heap in Python. By default Min Heap is implemented by this class. 
But we multiply each value by -1 so that we can use it as MaxHeap. 
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heapify(maxHeap)
        for i in range(k-1):
            heappop(maxHeap)
        return -maxHeap[0]
      
      
#OPTIMAL -  QUICK SELECT 
'''
Time: O(N) in the avarage case, O(N^2) in the worst case. Worst case happens when:
k = len(nums) and pivot is always the smallest element, so it divides array by [zero elements in the small, 
1 element in the equal, n-1 elements in the large], so it always goes to the right side with n-1 elements each time.
k = 1 and pivot is always the largest element, so it divides array by [n-1 elements in the small, 1 element in the equal,
zero elements in the large], so it always goes to the left side with n-1 elements reach time.

Space: O(N)
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       k = len(nums) - k

       def quickSelect(l,r):
           pivot, ptr = nums[r], l

           for i in range(l,r):
               if nums[i] <= pivot:
                   nums[ptr], nums[i] = nums[i], nums[ptr]
                   ptr += 1
           nums[ptr], nums[r] = nums[r], nums[ptr]

           if k < ptr: 
                return quickSelect(l, ptr - 1)

           elif k > ptr:
                return quickSelect(ptr + 1, r)

           else:
               return nums[ptr]

       return quickSelect(0, len(nums) - 1)



      


