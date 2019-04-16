int swap(int *xp, int *yp) 
{ 
    int temp = *xp; 
    *xp = *yp; 
    *yp = temp;
    return 0; 
} 
  
// A function to implement bubble sort 
int bubbleSort(int arr[], int n) 
{ 
   int i, j; 
   for (i = 0; i < n-1; i++){    
       // Last i elements are already in place    
       for (j = 0; j < n-i-1; j++){
           if (arr[j] > arr[j+1]){ 
              swap(&arr[j], &arr[j+1]);
           }
       }
   } 
   return 0;
} 
  
/* Function to print an array */
int printArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++){ 
        print_int( arr[i]); 
    }
    print_char(10); 
    return 0;
} 
  
// Driver program to test above functions 
int main() { 
    int arr[7]; 
    arr[0] = 64;
    arr[1] = 34;
    arr[2] = 25;
    arr[3] = 12;
    arr[4] = 22;
    arr[5] = 11;
    arr[6] = 90;
    bubbleSort(arr, 7);  
    printArray(arr, 7); 
    return 0; 
} 