/*
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.
Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

Constraints:
2 <= arr.length <= 105
arr.length is even.
1 <= arr[i] <= 105
*/

class Solution {
    public int minSetSize(int[] arr) {
        HashMap<Integer,Integer> freqmap = new HashMap<>();
        int n = arr.length;
        for(int i = 0; i < n; i++){
            freqmap.put(arr[i], freqmap.getOrDefault(arr[i],0) + 1);
        }
        
        int[] frequencies = new int[n+1];
        for(int freq : freqmap.values()){
            frequencies[freq]++;
        }
        
        int res = 0;
        int discarded = 0;
        int halfofarr = n / 2;
        int freq = n;
        
        while(discarded < halfofarr){
            res += 1;
            while(frequencies[freq] == 0) freq--;
            discarded += freq;
            frequencies[freq]--;
        }
        
        return res;
        
        
    }
}
