'''
BRUTE APPROACH
Sort and Insert

TC: O(n^2), where n is the length of stones, due to the nested inserts.
SC: O(1), no additonal data structures are used.
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            s1 = stones.pop()  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = stones.pop()  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                # the remaining stone will be s1-s2
                # loop through stones to find the index to insert the stone
                for i in range(len(stones)+1):
                    if i == len(stones) or stones[i] >= s1-s2:
                        stones.insert(i, s1-s2)
                        break
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain


'''
BETTER APPROACH
MAX HEAP

TC: O(nlogn); heappush() and heappop() both have O(logn) time complexity, and are both nested in the while loop. 
Note: heapify() runs in O(n) time, hence the time complexity is not affected.
SC: O(1); both the negation and the heapify are done in-place.

Unfortunately, Python's heap library implements a min-heap instead of a max-heap, whereby popping
will give us the lightest stone instead of the heaviest stone. The most common way to handle this, is to negate all the weight 
values of the stones. This way, the heaviest stone has the most negative value, and hence becomes the smallest value in the heap.
'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_heaviest = heapq.heappop(stones)
            second_heaviest = heapq.heappop(stones)

            if first_heaviest < second_heaviest:
                heapq.heappush(stones, first_heaviest - second_heaviest)

        stones.append(0)
        return abs(stones[0])
      
'''
Code explanation - 
Suppose,  [7,8] -> negate => [-7,-8]
now heappop(stones) as min heap => pops first_heaviest => -8
then heappop(stones) as min heap => pops second_heaviest => -7

"if first_heaviest < second_heaviest:" ensures that we actually have the heaviest stone as 1st heaviest (if we ignore the negation). 
So, first_heaviest = 8 is < second_heaviest = 7.

So we take differences of first_heaviest - second_heaviest = -8 - (-7) = -1.
We need to push negative values as we are implementing min heap, hence we subtract first_heaviest - second_heaviest.
We handle edge case by appending 0 to the stones array. So, If there are no stones left, stones[0] will return a 0. 

Then, all we have to do after obtaining the value from the heap is to un-negate the value to return the output. 
So, in the end we return abs value of stones[0]
'''

