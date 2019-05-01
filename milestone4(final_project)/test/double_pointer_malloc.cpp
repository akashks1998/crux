// int main(){
//     int r = 3, c = 4; 
//     int *arr = new(int)[r*c]; 
  
//     int i, j, count = 0; 
//     for (i = 0; i <  r; i++) {
//         for (j = 0; j < c; j++) {
//             *(arr + i*c + j) = ++count; 
//         }
//     }
//     for (i = 0; i <  r; i++) {
//         for (j = 0; j < c; j++) {
//             print_int(*(arr + i*c + j)); 

//         }
//     }
     
//    /* Code for further processing and free the  
//       dynamically allocated memory */
    
//    return 0; 


//     return 0;
// }

int main() 
{ 
    int r = 3, c = 4, i, j, count; 
  
    int **arr = new(int *)[r]; 
    for (i=0; i<r; i++) {
        arr[i] = new(int)[c]; 
    }
         
    // Note that arr[i][j] is same as *(*(arr+i)+j) 
    count = 0; 
    for (i = 0; i <  r; i++){
      for (j = 0; j < c; j++){
         arr[i][j] = ++count;  // OR *(*(arr+i)+j) = ++count  
      }
    }
  
    for (i = 0; i <  r; i++) {
        for (j = 0; j < c; j++){
            print_int(arr[i][j]);
        } 
    }
   /* Code for further processing and free the  
      dynamically allocated memory */
  
   return 0; 
} 