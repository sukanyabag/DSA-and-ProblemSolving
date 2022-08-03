/*
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start 
time of meeting i and end[i] is finish time of meeting i. What is the maximum number of meetings that can be accommodated in the 
meeting room when only one meeting can be held in the meeting room at a particular time?
 
Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


Example 1:

Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output: 
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)

Your Task :
You don't need to read inputs or print anything. 
Complete the function maxMeetings() that takes two arrays start[] and end[] along with their 
size N as input parameters and returns the maximum number of meetings that can be held in the meeting room.


Expected Time Complexity : O(N*LogN)
Expected Auxilliary Space : O(N)


Constraints:
1 ≤ N ≤ 105
0 ≤ start[i] < end[i] ≤ 105
*/

class Solution 
{
    //Function to find the maximum number of meetings that can
    //be performed in a meeting room.
    public static int maxMeetings(int startMeeting[], int endMeeting[], int n){
        ArrayList<Meeting> meet = new ArrayList<>();
        
        for(int i=0; i < startMeeting.length; i++){
            meet.add(new Meeting(startMeeting[i], endMeeting[i], i+1));
        }
        
        MeetingComparator mc = new MeetingComparator();
        Collections.sort(meet,mc);

        ArrayList<Integer> res = new ArrayList<>();
        
        res.add(meet.get(0).posMeeting);
        int lim = meet.get(0).endMeeting;
        
        for(int i=0; i < startMeeting.length; i++){
            if(meet.get(i).startMeeting > lim){
                lim = meet.get(i).endMeeting;
                res.add(meet.get(i).posMeeting);
            }
        }
        return res.size();  
    }
}

class Meeting{
    int startMeeting;
    int endMeeting;
    int posMeeting;
    
    Meeting(int startMeeting, int endMeeting, int posMeeting){
        this.startMeeting = startMeeting;
        this.endMeeting = endMeeting;
        this.posMeeting = posMeeting;
    }
}

class MeetingComparator implements Comparator<Meeting>{
        
    @Override
    public int compare(Meeting m1, Meeting m2){
        if(m1.endMeeting < m2.endMeeting)
            return -1;
        else if(m1.endMeeting > m2.endMeeting)
            return 1;
        else if(m1.posMeeting < m2.posMeeting)
            return -1;
        return 1;
    }
}
