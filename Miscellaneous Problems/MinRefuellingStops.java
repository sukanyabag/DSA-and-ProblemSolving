/*
A car travels from a starting position to a destination which is target miles east of the starting position.
There are gas stations along the way. The gas stations are represented as an array stations where 
stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.
The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. 
When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
Return the minimum number of refueling stops the car must make in order to reach its destination.
If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.
If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.

Constraints:
1 <= target, startFuel <= 109
0 <= stations.length <= 500
0 <= positioni <= positioni+1 < target
1 <= fueli < 109
*/

class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        //edge case - can reach the target without stopping
        if(startFuel >= target) return 0;
        
        //push all fueli in descending order in priority queue
        // greedy-logic - maxDist depends on amount of fuel at ith station
        // if we refill with highest fuel value, we will need minimum stops
        Queue<Integer> q = new PriorityQueue<>((a , b) -> b - a);
        
        int i = 0;
        int n = stations.length;
        int maxDist = startFuel;
        int minStops = 0;
        
        //as long as maxDIst travelled is less than target, loop
        while(maxDist < target){
            //loop over stations' and check if positioni in stations[][] is less than maxDist
            //we can travel. If yes, then keep on adding fueli available at those positioni
            //into the queue in descending order(so we get the max fuel as possible)
            while(i < n && stations[i][0] <= maxDist){
                q.offer(stations[i][1]);
                i++;
            }
            
            //can never reach the target(when stations[i][0] > maxDist)
            //so nothing gets added to the queue, and it's empty
            //hence return -1
            if(q.isEmpty()) return -1;
            
            //update maxDist after refilling it with highest fuel available
            maxDist += q.poll();
            
            //increment minStops as well to store final answer
            minStops += 1;
        }
        
       return minStops; 
    }
}
