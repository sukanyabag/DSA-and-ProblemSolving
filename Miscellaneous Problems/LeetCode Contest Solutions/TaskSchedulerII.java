/*
    You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type
    of the ith task.

    You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task 
    before another task of the same type can be performed.

    Each day, until all tasks have been completed, you must either:

    Complete the next task from tasks, or
    Take a break.
    Return the minimum number of days needed to complete all tasks.

    Input: tasks = [1,2,1,2,3,1], space = 3
    Output: 9
    Explanation:
    One way to complete all tasks in 9 days is as follows:
    Day 1: Complete the 0th task.
    Day 2: Complete the 1st task.
    Day 3: Take a break.
    Day 4: Take a break.
    Day 5: Complete the 2nd task.
    Day 6: Complete the 3rd task.
    Day 7: Take a break.
    Day 8: Complete the 4th task.
    Day 9: Complete the 5th task.
    It can be shown that the tasks cannot be completed in less than 9 days.

    Input: tasks = [5,8,8,5], space = 2
    Output: 6
    Explanation:
    One way to complete all tasks in 6 days is as follows:
    Day 1: Complete the 0th task.
    Day 2: Complete the 1st task.
    Day 3: Take a break.
    Day 4: Take a break.
    Day 5: Complete the 2nd task.
    Day 6: Complete the 3rd task.
*/

class Solution {
    public long taskSchedulerII(int[] tasks, int space) {
        // Map stores the task as key and when it was last done as value
        HashMap<Integer, Long> map = new HashMap<>();
        long minDays = 0;
        // We take each task and asssign their days
        for (int task: tasks) {
            // If we have already done a task of similar type then...
            if (map.containsKey(task)) {
                // We check on which day it was last done
                long lastDay = map.get(task);
                // then we assign the task to the day when it can be assigned next
                // we take maximum of (lastDay + space and minDays) + 1, to ensure
                // that its not preoccupied by any other task
                long assignDay = Math.max(lastDay + space, minDays) + 1L;
                
                // We update the task with its newly assigned day in the map
                map.put(task, assignDay);
                
                // Update minDays
                minDays = Math.max(minDays, assignDay);
            }
            // If we encounter a new task, we put it in the map and increment 
            // minDays
            else {
                map.put(task, minDays + 1);
                minDays++;
            }
        }
        
        return minDays;
    }
}
