// C++ program to find union of 
// two sorted arrays 

using namespace std; 

/* Function prints union of arr1[] and arr2[] 
m is the number of elements in arr1[] 
n is the number of elements in arr2[] */
int printUnion(int arr1[], int arr2[], int m, int n) 
{ 
int i = 0, j = 0; 
while (i < m && j < n) 
{ 
    if (arr1[i] < arr2[j]) 
    cout << arr1[i++] << "hello"; 
    
    else if (arr2[j] < arr1[i]) 
    cout << arr2[j++] << " "; 
    
    else
    { 
    cout << arr2[j++] << " "; 
    i++; 
    } 
} 

/* Print remaining elements of the larger array */
while(i < m) 
    cout << arr1[i++] << " "; 

while(j < n) 
    cout << arr2[j++] << " "; 
} 

/* Driver program to test above function */
int main() 
{ 
int arr1[] = {1, 2, 4, 5, 6}; 
int arr2[] = {2, 3, 5, 7}; 
    
int m = sizeof(arr1)/sizeof(arr1[0]); 
int n = sizeof(arr2)/sizeof(arr2[0]); 
    
// Function calling 
printUnion(arr1, arr2, m, n); 

return 0; 
} 