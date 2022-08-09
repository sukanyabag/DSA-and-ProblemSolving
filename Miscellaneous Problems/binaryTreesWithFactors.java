/* QUESTION - 
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
We make a binary tree using these integers, and each number may be used for any number of times. 
Each non-leaf node's value should be equal to the product of the values of its children.
Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
Example 1:
Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Constraints:
1 <= arr.length <= 1000
2 <= arr[i] <= 109
All the values of arr are unique.
-------DRY RUN -------
arr = [2,4,5,10]
dp = [1, 1, 1, 1] 
// all elements of DP table are 1 because every element of the array without any children is a tree in itself
i = 0, j = 0
// Wont run becoz j < i -> false
------------------------------
i = 1, j = 0
arr[i] = 4, arr[j] = 2
arr[i] % arr[j] == 0 - true
rem = arr[i] / arr[j] = 4 / 2 = 2
dp[i] = 1, dp[j] = 1
dp[i] += dp[j] * dp[map.get(rem)] = 1 * 1 = 1
dp[i] = dp[i] + 1 = 2
dp = [1, 2, 1, 1] 
-------------------------------
i = 2, j = 0
arr[i] = 5, arr[j] = 2
arr[i] % arr[j] == 0 - false
i = 2, j = 1
arr[i] = 5, arr[j] = 4
arr[i] % arr[j] == 0 - false
-------------------------------
i = 3, j = 0
arr[i] = 10, arr[j] = 2
arr[i] % arr[j] == 0 - true
rem = arr[i] / arr[j] = 10 / 2 = 5
dp[i] = 1, dp[j] = 1
dp[i] += dp[j] * dp[map.get(rem)] = 1 * 1 = 1
dp[i] = dp[i] + 1 = 2
------ dp = [1, 2, 1, 2] ------ 
i = 3, j = 1
arr[i] = 10, arr[j] = 4
arr[i] % arr[j] == 0 - false
i = 3, j = 2
arr[i] = 10, arr[j] = 5
arr[i] % arr[j] == 0 - true
rem = arr[i] / arr[j] = 10 / 5 = 2
dp[i] = 2, dp[j] = 1
dp[i] += dp[j] * dp[map.get(rem)] = 1 * 1 = 1
dp[i] = dp[i] + 1 = 2 + 1 = 3
------ dp = [1, 2, 1, 3] ----------
*/


class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
        int n = arr.length;
        
        //base case
        if(n == 1) return 1;
        
        Arrays.sort(arr);
        
        
        long[] dp = new long[n];
        Arrays.fill(dp, 1);
        
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < n; i++){
            map.put(arr[i],i);
        }
        
        long res = 0;
        
         for(int i = 0; i < n; i++){
            int c = arr[i];
            for(int j = 0; j < i; j++){
                int a = arr[j];
                if(c % a == 0){
                    int b = c / a; // as a * b == c
                    if(map.containsKey(b)){
                        dp[i] += dp[j] * dp[map.get(b)];
                    }
                }
            }
        }
        
        for(long x : dp){
            res += x;
        }
        
        return (int) (res % 1000000007);
        
    }
}

/* 
Important points while approaching the problem -
We need to give each element in the array a chance to be a root node and since its childrens' multiplication is supposed to equal it,
it is better if we sort the array and then move an i pointer ahead being the root and j pointer moving till i. ie) i from 0 to array.length and j from 0 to i - 1.
While moving with i pointer if we find a j that divides arr[i], then we might have a solution because - If a * b == c, where a is the 
arr[j] and c is the arr[i], we have a solution because acco to the problem, b can be equal to a ie) can be repeated. If not, we can find
a b eventually by setting a variable called b= c / a and see if it exists in the array and if it does, it is the other child of the a, b and c subtree/tree.
Use a hashmap to map elements to indexes while finding the b as said above
We can use a DP table to track this down where initially all elements of DP table are 1 because every element of the array without any children 
is a tree in itself. If the last two points above help us find an a, b, c pair, update the dp[c] = dp[a] * dp[b] as it will cover all the cases 
like c being the root, a the right child and b left child and c being the root, a the left child and b right child.
The final solution will be sum of values of the DP table. 
*/
