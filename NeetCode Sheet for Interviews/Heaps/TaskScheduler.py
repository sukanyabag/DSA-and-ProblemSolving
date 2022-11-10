'''
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, 
the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks 
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Constraints:
1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
'''

'''
OPTIMAL SOLUTION USES MAX HEAP

TC - O(N * M)
(N = COUNT TASKS AND PUSH THEM IN HEAP, M = IDLE TIME OF CPU (IN WORST CASE WE HAVE TO BE ENTIRELY IDLE WHERE ALL TASKS ARE SAME EX: [A,A,A,A,A,A,A...])

SC - O(N)
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #store counts of tasks
        taskCnt = Counter(tasks)
        #store task counts in maxheap (negate values since by default python has minheap)
        mxHeap = [-tcnt for tcnt in taskCnt.values()]
        #heapify the maxheap
        heapify(mxHeap)

        #stores and updates units of time
        time = 0
        #pairs of [-tcnt, idleTime] idleTime -> at what time the task can be done again
        que = deque()
        #continue processing tasks until maxheap or queue is empty
        while mxHeap or que:
            #at every loop increment time by 1
            time += 1
            #if maxheap non empty keep on popping from it
            #update the tcnt (taskcount) by adding 1 (for neg vals add 1)
            if mxHeap:
                tcnt = 1 + heappop(mxHeap)
                #then append the tcnt to the queue if tcnt is non zero
                #q[0][1] = idleTime = current_time + n(cooldown)
                if tcnt:
                    que.append([tcnt, time + n])

            #if idletime == time, then pop the task from queue and push to maxheap
            #as it can be done again
            if que and que[0][1] == time:
                heappush(mxHeap, que.popleft()[0])
        #return min time taken
        return time
  

