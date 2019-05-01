// Fibonacci Series using Space Optimized Method 
int fib(int n) 
{ 
  int a = 0, b = 1, c, i; 
  if( n == 0){
    return a; 
  }
  for (i = 2; i <= n; i++) 
  { 
     c = a + b; 
     a = b; 
     b = c; 
  } 
  return b; 
} 
  
int main () 
{ 
  int n;
  print_char('n'); print_char('?');
  scan_int(n);
  print_int(fib(n)); 
  return 0; 
} 
