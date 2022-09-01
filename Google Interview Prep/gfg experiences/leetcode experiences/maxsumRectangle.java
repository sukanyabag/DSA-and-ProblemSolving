/**
Algorithmic Question: Given a grid of size m * n, find the maximum sum rectangle from the grid.

Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.

1 2 3 4 5
3 4 5 6 4
4 5 6 7 3 
5 6 7 8 2



r1, c1 

... r2,c2

n2 * n4 = n6 very bad tc
optimised - take every col pairs and add themup + apply kadane
o(c2)+ create an arr from it O(R) + O(R) kadane on the arr

c0->c1 c1->c2
c0->c2 c1-c3
'''   ''''
c0-cn c1-cn ....

apply kadane on every colsum
O(rC**2) = much better than on6

**/

// User function Template for Java

class Solution {
    int kadane(int[] arr){
        int maxsum = Integer.MIN_VALUE;
        int sum = 0;
        for(int i = 0;i<arr.length;i++){
            sum+=arr[i];
            maxsum = Math.max(sum,maxsum);
            if(sum<0){
                sum = 0;
            }
        }
        return maxsum;
    }
    int maximumSumRectangle(int R, int C, int M[][]) {
        int maxsum = Integer.MIN_VALUE;
        for(int i = 0;i<C;i++){
            int[] tmp = new int[R];
            for(int j=i;j<C;j++){
                for(int k = 0;k<R;k++){
                    tmp[k]+=M[k][j];
                }
                int sum = kadane(tmp);
                if(sum>maxsum){
                    maxsum = sum;
                }
            }
        }
        return maxsum;
    }
};
