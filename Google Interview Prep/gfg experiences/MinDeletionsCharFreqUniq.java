/*
Step 1: Take all the characters and their count in a HashMap
Step 2: Now take a Hash Set to store the unique frequencies and initialize delete count to 0
Step 3: Now check if the frequency is present in the set . If not then simply add
Step 4: If it contains then take a loop and keep on decreasing the frequency & increasing the delete count by 1 until the value is not contained in the set and if the final value of frequency is greater than 0 then add it in the set.

*/

class Solution {
public int minDeletions(String s) {
int count = 0;

    HashMap<Character,Integer> hm = new HashMap<>();
    char ch[] = s.toCharArray();
    for(int i = 0; i<ch.length ; i++)
    {
        hm.put(ch[i],hm.getOrDefault(ch[i],0)+1);
    }
    
    Set<Integer> set = new HashSet<>();
    for(char c: hm.keySet())
    {
        int freq = hm.get(c);
        if(!set.contains(freq))set.add(freq);
        else{
            while(freq> 0 && set.contains(freq))
            {
                freq--;
                count++;
            }
            if(freq>0)set.add(freq);
        }
    }
    return count;
}
}
