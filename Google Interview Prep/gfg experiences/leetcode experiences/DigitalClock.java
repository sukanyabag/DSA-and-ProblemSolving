/*
First interview: 28/01/2022. I got one question which sounded like this: You have a digital clock that shows the time using the AM and PM format. 
That clock also has 4 buttons which add to the time 1 minute, 5 minutes, 10 minutes respectively 15 minutes.
You are given a future time. Get the least amount of presses to get the desired time.
*/

// "static void main" must be defined in a public class.
public class Main {
public static void main(String[] args) {
String now = "03:27PM";
String future = "03:57PM"; //outputs 2 - 15+15 two ops

    System.out.println(countSteps(now, future));
    // System.out.println(convertTo24Hr(future, false));
}

public static int countSteps(String now, String future) {
    String formatNow = now.substring(5, 7);
    String formatFut = future.substring(5, 7);
    boolean isNowPM = false;
    boolean isFutPM = false;
    if (formatNow.equals("PM"))
        isNowPM = true;
    
    if (formatFut.equals("PM"))
        isFutPM = true;
    
    int counter = 0;
    
    int now_mins = convertTo24Hr(now, isNowPM);
    int fut_mins = convertTo24Hr(future, isFutPM);
    
    while(now_mins < fut_mins){
        if(now_mins + 15 <= fut_mins){
            now_mins += 15;
            counter++;
        }
        
        else if(now_mins + 10 <= fut_mins){
            now_mins += 10;
            counter++;
        }
        
        else if(now_mins + 5 <= fut_mins){
            now_mins += 5;
            counter++;
        }
        
        else{
            now_mins += 1;
            counter++;
        }
    }
    
    return counter;
}

private static int convertTo24Hr(String time, boolean isPM) {
    // 03:45PM
    // 0123456
    int hr = Integer.valueOf(time.substring(0, 2));
    int min = Integer.valueOf(time.substring(3, 5));
    if (isPM) {
        hr += 12;
    }
    min += hr * 60;
    return min;
}
