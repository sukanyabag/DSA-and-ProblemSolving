/*
Write a function to return minimum and maximum in an array. Your program should make the minimum number of comparisons. 
input - {1000, 11, 445, 1, 330, 3000}
output-
Minimum element is 1
Maximum element is 3000
*/
public class App{
    static class MinMaxPair{
        int min;
        int max;
    }

    static MinMaxPair findMinMax(int arr[], int n){
        MinMaxPair minmax = new MinMaxPair();
        int i;
    
    //If there is only one element then return it as min and max both
    if (n==1) {
        minmax.max = arr[0];
        minmax.min = arr[0];
    }
    
    //If there are more than one elements, then initialize min and max
    if (arr[0] > arr[1]) {
        minmax.max = arr[0];
        minmax.min = arr[1];
    }
    else {
        minmax.max = arr[1];
        minmax.min = arr[0];
    }
    
    for (i=2; i<n; i++){
        if(arr[i] > minmax.max){
            minmax.max = arr[i];
        } 
        else if (arr[i] < minmax.min){
            minmax.min = arr[i];
        }
    }
    
    return minmax;
    
    }

/* Driver program to test above function */
    public static void main(String args[]) {
        int arr[] = {90,87,56,41,23};
        int n = 5;
        MinMaxPair minmax = findMinMax(arr, n);
        System.out.println("\nMinimum element is " + minmax.min);
        System.out.println("\nMaximum element is " + minmax.max);
 
    }
 
}
