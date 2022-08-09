/*
	There are N rooms. You are given a binary string and a value X. S[i] = '1' represents
	room with WiFi and S[i] = '0' represents room without WiFi. X is the range of wifi
	If S[i] = '1' and X = 3, it denotes the room can provide wifi upto 3 rooms in either 
	direction. 

	Find whether all rooms get wifi or not.

	Input:
	N = 3, X = 0
	S = "010"
	Output:
	0
	Explanation: 
	Wifi is only accessible in second room.

	Input:
	N = 5, X = 1
	S = "10010"
	Output:
	1
	Explanation: 
	Wifi range goes in all rooms.

*/

package Misc.GFGInterviewSeries;

public class WifiRange {
	public static void main(String[] args) {
		
	}

	public static boolean wifiRange(int N, String S, int X) {
		// EG: S = "10010" X = 1
        int wifi[] = new int[N];
        // wifi[] = [0, 0, 0, 0, 0]
        int assign = 0;

        for (int i = 0; i < N; i++) {
        	// If we encounter a '1', we assign that index in wifi as MAX_VALUE
        	// and set assign to X
            if (S.charAt(i) == '1') {
                assign = X;
                wifi[i] = Integer.MAX_VALUE;
            }
            // Otherwise we set wifi[i] to assign if assign is +ve, or set it to 0
            else {
                wifi[i] = Math.max(assign, 0);
                assign--;
            }
        }
        // wifi[] = [MAX_VALUE, 1, 0, MAX_VALUE, 1]
        assign = 0;
        for (int i = N - 1; i >= 0; i--) {
            if (S.charAt(i) == '1') {
                assign = X;
            }
            else if (wifi[i] == 0){
                wifi[i] = Math.max(assign, 0);
                assign--;
            }
        }
        // wifi[] = [MAX_VALUE, 1, 1, MAX_VALUE, 1]

        for (int num: wifi) {
            if (num <= 0)
                return false;
            // System.out.print(num + " ");
        }
        
        return true;
    }
}
