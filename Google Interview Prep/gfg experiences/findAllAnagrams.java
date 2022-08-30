class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList();//This is the final result list
        if(s.length()==0 || s == null) return res;
        int [] occur = new int[26];//a-z 26 letters
        for(char c : p.toCharArray()) occur[c-'a']++;//we store there occurence in occur list
        int left = 0,right = 0,count = p.length();
        while(right<s.length()){
		//We check and increment/decrement if right index char of s is present in the occur list
		   //And if it is then increment right and decrement the occurence of that character and count
		   //** right will always increment
            if(occur[s.charAt(right++)-'a']-->=1) count--;
			
			//If count is zero then we can say that the window between left and right is an anagram, therefor add left in the list
            if(count == 0) res.add(left);
			
			//At some point if we do/don't find the anagram and right-left size if equal to p size and we have to shift the window and increment left and occurance of removed/shifted char and increment the count
			//** left will not always increment as it will check the first condition first
            if(right-left==p.length() && occur[s.charAt(left++)-'a']++>=0) count++;
        }
        return res;
    }
}
