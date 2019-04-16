int fun(int *ptr,int arr[], int a, int b, int c, int d, int e, int f, int g ){ 
    *ptr = 30; 
    arr[1] = 400;
    int ret = (a + b + c + d + e + f + g ) / 2;
    return ret;
} 
   
int main() 
{ 
  int x = 20; 
  int arr[7];
  for (int i=0; i < 7; i++ ){
      arr[i] = i * i;
  }
  int a = fun(&x, arr, arr[0], arr[1] , arr[2], arr[3], arr[4], arr[5], arr[6]);
  print_int(x);
  print_int(a); 
  print_int(arr[1]);
  return 0; 
} 