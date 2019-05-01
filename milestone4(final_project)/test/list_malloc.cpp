int main(){ 
    int n = 12;
    int arr[12];
    // int *arb = &arr[0];
    int *s = new(int);
    print_int(s);
    int *arb = new (int)[12]; 
    for(int i=0; i< n; i++){
        arb[i] = 50 * i;
    }
    
    int *a = arb;
    for(int i=0; i<n; i++){
        print_int(a[i]);
    }
    return 0; 
}