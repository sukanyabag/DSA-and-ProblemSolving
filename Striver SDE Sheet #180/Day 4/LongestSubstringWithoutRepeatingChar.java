/*
Problem Statement: Given a String, find the length of longest substring without any repeating character.
Examples:
Example 1:
Input: s = ”abcabcbb”
Output: 3
Explanation: The answer is abc with length of 3.
*/

import java.util.*;
public class Solution {
    static int solve(String s) {
        HashMap < Character, Integer > mpp = new HashMap < Character, Integer > ();

        int left = 0, right = 0;
        int n = s.length();
        int len = 0;
        while (right < n) {
            if (mpp.containsKey(s.charAt(right))) left = Math.max(mpp.get(s.charAt(right)) + 1, left);

            mpp.put(s.charAt(right), right);

            len = Math.max(len, right - left + 1);
            right++;
        }
        return len;
    }
