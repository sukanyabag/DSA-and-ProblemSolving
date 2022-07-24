/*  
You are given two strings current and correct representing two 24-hour times.
24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. 
The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. 
You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.

Example 1:
Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer than 3 operations.

Constraints:
current and correct are in the format "HH:MM"
current <= correct
*/

class Solution {
    public int convertTime(String current, String correct) {
        //call helper func to convert time to mins on current and correct inputs
        int curr_mins = convertToMins(current);
        int corr_mins = convertToMins(correct);
        
        //init counter to store minops required to convert current to correct. 
        int counter = 0;
        
        while(curr_mins < corr_mins){
            //keep on greedily adding 60mins (1hr) until curr_min + 60 <= corr_min
            //increment counter to count iterations each time
            if(curr_mins + 60 <= corr_mins){
                curr_mins += 60;
                counter++;
            }
            
            //else keep on greedily adding 15mins until curr_min + 15 <= corr_min
            //increment counter to count iterations each time
            else if(curr_mins + 15 <= corr_mins){
                curr_mins += 15;
                counter++;
            }
            
            //else keep on greedily adding 5mins until curr_min + 5 <= corr_min
            //increment counter to count iterations each time
            else if(curr_mins + 5 <= corr_mins){
                curr_mins += 5;
                counter++;
            }
            
            //else keep on greedily adding 1min until curr_min + 1 <= corr_min
            //increment counter to count iterations each time
            else{
                curr_mins += 1;
                counter++;
            }
        }
        
        return counter;
    }
    
    //this helper func converts given time strings to minutes
    public int convertToMins(String time){
        //extract hour part from time string (02:30) - 02
        int h = Integer.valueOf(time.substring(0,2));
        //extract mins part from time string (02:30) - 30
        int m = Integer.valueOf(time.substring(3,5));
        
        //self explanatory hrs to min conversion
        int result = 60*(h) + m;
        
        
        return result;
        
    }
}
