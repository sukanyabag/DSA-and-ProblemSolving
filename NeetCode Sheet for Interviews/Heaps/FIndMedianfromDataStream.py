'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, 
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
'''

class MedianFinder:
    def __init__(self):
        self.smolmaxheap = []
        self.bigminheap = []

    #add elements into smolmaxheap by default
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smolmaxheap, -1 * num)
        #case 1 - each elm in smolmaxheap should be <= each elm in bigminheap
        if (self.smolmaxheap and self.bigminheap
            and (-1 * self.smolmaxheap[0]) > self.bigminheap[0]):
            val = -1 * heapq.heappop(self.smolmaxheap)
            heapq.heappush(self.bigminheap, val)

        #case 2 - uneven size of heaps
        if len(self.smolmaxheap) > len(self.bigminheap) + 1:
            val = -1 * heapq.heappop(self.smolmaxheap)
            heapq.heappush(self.bigminheap, val)

        if len(self.bigminheap) > len(self.smolmaxheap) + 1:
            val = heapq.heappop(self.bigminheap)
            heapq.heappush(self.smolmaxheap, -1 * val)
   
    def findMedian(self) -> float:
        if len(self.smolmaxheap) > len(self.bigminheap):
            return -1 * self.smolmaxheap[0]
        if len(self.bigminheap) > len(self.smolmaxheap):
            return self.bigminheap[0]

        return (-1 * self.smolmaxheap[0] + self.bigminheap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
