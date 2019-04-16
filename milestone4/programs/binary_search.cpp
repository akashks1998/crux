// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int* arr, int l, int r, int x) 
{ 
    if (r >= l) { 
        int mid = l + (r - l) / 2; 
  
        // If the element is present at the middle 
        // itself 
        if (arr[mid] == x) {
            return mid; 
        }
  
        // If element is smaller than mid, then 
        // it can only be present in left subarray 
        if (arr[mid] > x) {
            return binarySearch(arr, l, mid - 1, x); 
        }
  
        // Else the element can only be present 
        // in right subarray 
        return binarySearch(arr, mid + 1, r, x); 
    } 
  
    // We reach here when element is not 
    // present in array 
    return -1; 
} 

int nothere(){
    // print_char('n');print_char('o');print_char('t');print_char(' ');print_char('h');print_char('e');print_char('r');print_char('e');print_char('.');
    print_char('n');print_char('o');
    return 0;
}

int newline(){
    int a=10;
    char c=a;
    print_char(c);
    return 0;
}

int space(){
    int a=20;
    char c=a;
    print_char(c);
    return 0;
}

int here(int result){
    // print_char('p');print_char('r');print_char('e');print_char('s');print_char('e');print_char('n');print_char('t');print_char(' ');print_char('a');print_char('t');print_char(' ');print_int(result);
    print_char('y');print_char('e');print_char('s');
    print_int(result);
    return 0;
}
  
int main() 
{ 
    int n;
    print_char('n');print_char('?');newline();
    scan_int(n);
    print_char('e');print_char('l');print_char('e');print_char('m');print_char('e');print_char('n');print_char('t');print_char('s');print_char('?');newline();
    int* arr = new(int)[n];
    for(int i=0;i<n;i++){
        scan_int(arr[i]);
    }
    print_char('s');print_char('e');print_char('a');print_char('r');print_char('c');print_char('h');print_char('f');print_char('o');print_char('r');print_char('?');newline();
    int x;
    scan_int(x);
    int result = binarySearch(arr, 0, n - 1, x);
    if(result == -1){
        nothere();
    }else{
        here(result);
    }
    return 0; 
}