/* 
Given an array (or string), the task is to reverse the array/string.
Examples : 

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

*/

public class App{
    
    static void reverseArray(int arr[], int beg, int des) {
        int tmp;
        
        while (beg<des){
            tmp = arr[beg];
            arr[beg] = arr[des];
            arr[des] = tmp;
            beg++;
            des--;
        }
    
    }
    
    static void printResult(int arr[], int n){
        for (int i=0; i<n; i++){
            System.out.println(arr[i] + " ");
		 
		System.out.println();
        }
    }
    public static void main(String args[]) {
		
		int arr[] = {1, 2, 3, 4, 5, 6};
		printResult(arr, 6);
		reverseArray(arr, 0, 5);
		System.out.println("Reversed array is \n");
		printResult(arr, 6);
		
	}
  
}


PYTHON 3X
def reverseList(arr, beg, des):
    while beg < des:
        arr[beg], arr[des] = arr[des], arr[beg]
        beg += 1
        des -= 1
