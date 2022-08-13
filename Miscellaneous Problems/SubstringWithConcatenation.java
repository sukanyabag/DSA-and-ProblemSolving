/*  
You are given a string s and an array of strings words of the same length. 
Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.

Solution: (HASHMAP WITH SLIDING WINDOW APPROACH)
- We calculate word length & total words, create a frequency map of given words
- Now we iterate each index & check if word exists in frequency map
- If doesn't exists then break. 
- We also take seenWords map, where we put words which are seen in for this index 
- If seenWords value is more than actual frequency exists, then also we break
- If totalWords are equal to the found words, then we add the index in result. 
- At last, we return result

Time Complexity: O(n * m * length), where n is number of values in array, m is total words & length is each word length 
Space Complexity: O(m)
*/

class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        //base case
        if(s == null || s.length() == 0 || words == null || words.length == 0){
            return new ArrayList<>();
        }
        
        //init hashmap to store word as key and its frequency as val
        HashMap<String,Integer> freqMap = new HashMap<>();
        
        //loop over freq map and add all words in words list
        for(String word : words){
            freqMap.put(word, freqMap.getOrDefault(word,0)+1);
        }
        
        //store length of each word in words 
        int lenOfword = words[0].length();
        //count total num of words
        int totWords = words.length;
        //calculate total length of words in words list (words are of same length)
        int totWordLen = lenOfword * totWords;
        
        //init result array
        List<Integer> res = new ArrayList<>();
        
        for(int i = 0; i <= s.length() - totWordLen; i++){
            //creating hashmap for seen words to ignore them if found repeating in s
            HashMap<String,Integer> seenWord = new HashMap<>();
            
            
            for(int j = 0; j < totWords; j++){
                //fetch word index
                int wordIdx = i + j * lenOfword;
                //get the word
                String word = s.substring(wordIdx, wordIdx + lenOfword);
                
                //if word not found in freqmap, simply break
                if(!freqMap.containsKey(word)) break;
                
                //otherwise put that word in seenword map
                seenWord.put(word, seenWord.getOrDefault(word,0)+1);
                
                //if word count in seenword map is more than it appears in freqmap, break
                if(seenWord.get(word) > freqMap.getOrDefault(word,0)) break;
                
                //if totWords are found then simply add idx of occurence to result
                if(j+1 == totWords){
                    res.add(i);
                }
                
            }
        
            
        }
        
        return res;
        
    }
}

