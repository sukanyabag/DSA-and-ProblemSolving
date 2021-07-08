'''
Q- Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 
Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++){
            char curr = s.charAt(i);
            if(!map.containsKey(curr)){
                map.put(curr, i);
            }
            else{
                map.put(curr, -1);
            }
        }
        int min = Integer.MAX_VALUE;
        for(char c : map.keySet()){
            if(map.get(c)>-1 && map.get(c)< min){
                min = map.get(c);
            }
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }
}
