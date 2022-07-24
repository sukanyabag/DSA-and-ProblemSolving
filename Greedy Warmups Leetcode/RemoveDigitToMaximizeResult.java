/* 
You are given a string number representing a positive integer and a character digit.
Return the resulting string after removing exactly one occurrence of digit from number such that the value 
of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

Example 1:
Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".

Constraints:
2 <= number.length <= 100
number consists of digits from '1' to '9'.
digit is a digit from '1' to '9'.
digit occurs at least once in number.
*/

class Solution {
    public String removeDigit(String number, char digit) {
        String maxval = "";
        
        for(int i =0; i < number.length(); i++){
            //if char at i equals digit 
            if(number.charAt(i) == digit){
                //remove that char and update num to rest of the substring after that removed char
                String num = number.substring(0,i) + number.substring(i+1);
                //compare strings stored in num with maxval
                int n = num.compareTo(maxval);
                //if string present in num is greater than str stored in maxval
                if(n>0){
                    //then update maxval to num 
                    maxval = num;
                }
            }
        }
        return maxval;
    }
}
