/*
* Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The 
 * stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,
 * 000,000).
 * 
 * His C (2 <= C <= N) cows don't like this barn layout and become aggressive 
 * towards each other once put into a stall. To prevent the cows from hurting each 
 * other, FJ wants to assign the cows to the stalls, such that the minimum distance 
 * between any two of them is as large as possible. What is the largest minimum 
 * distance?


OPTIMAL APPROACH
Time Complexity: O(N*log(M)). 
Reason: For binary search in a space of M, O(log(M))  and for each search, we iterate over max N stalls to check. O(N).
Space Complexity: O(1)
*/
	
	public static void aggressiveCows(int[] stalls, int c) {
    int n  = stalls.length;
		Arrays.sort(stalls);
		
		int low = 1, high = stalls[n - 1] - stalls[0];
    int res = 0;
		while (low <= high) {
			int mid = (low + high) / 2;
			if (isPossible(stalls, mid, c)) {
                res = mid;
				low = mid + 1;
			}
			else {
				high = mid - 1;
			}
		}
		return res;
	}
	
	public static boolean isPossible(int[] stalls, int minDist, int c) {
		int cows = 1;
		int lastCowPosition = stalls[0];
		
		for (int i = 1; i < n; i++) {
			if (stalls[i] - lastCowPosition >= minDist) {
				cows++;
				lastCowPosition = stalls[i];
                if (cows >= c)
			        return true;
			}
		}
		return false;
	}
}
