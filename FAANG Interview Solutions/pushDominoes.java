/** 
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
**/

class Solution {
    public String pushDominoes(String string) {
        char[] dominoes = string.toCharArray();
        int N  = dominoes.length;
        int[] forces = new int[N];
        
        int force = 0;
        for (int i = 0; i<N; i++){
            if(dominoes[i] == 'R'){
                force = N;
            }
            else if (dominoes[i] == 'L'){
                force = 0;
            }
            else{
                force = Math.max(force-1,0);
            }
            forces[i]  += force;
        }
        
        force = 0;
        for (int i = N-1;i>=0;i--){
            if(dominoes[i] == 'L'){
                force = N;
            }
            
            else if (dominoes[i] == 'R'){
                force = 0;
            }
            else{
                force = Math.max(force-1,0);
            }
            forces[i]  -= force;
        }
        
        StringBuilder res = new StringBuilder();
        
        for (Integer f: forces){
            if (f>0){
                res.append('R');
            }else if (f<0){
                res.append('L');
            }else{
                res.append('.');
            }
        }
        
        return res.toString();
    }
}
