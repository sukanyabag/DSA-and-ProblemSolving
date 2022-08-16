/*
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
*/

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        List<String> path = new ArrayList<>();
        findPartitions(0,s,path,res);
        return res;
    }
    
    void findPartitions(int idx, String s, List<String> path, List<List<String>> res){
        //base case -> if partition is complete (idx reaches end of string)
        if(idx == s.length()){
            res.add(new ArrayList<>(path));
            return;
        }
        
        //otherwise, keep finding palindrome partitions
        for(int i = idx; i < s.length(); i++){
            // if string from idx -> i is palindrome, add it to path
            if(isPalindrome(s,idx,i)){
                path.add(s.substring(idx, i+1));
                //then make recursive call to find paritions from next idx (i+1)
                findPartitions(i+1, s, path,res);
                //remove last path appended for backtracking 
                path.remove(path.size() - 1);
            }
        }    
    }
    
    boolean isPalindrome(String s, int beg, int end){
        while(beg <= end){
            if(s.charAt(beg++) != s.charAt(end--)) return false;
        }
        
        return true;
    }
}
