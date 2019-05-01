float avg(float a[], int n){
    float avg;
    float sum = 0;
    for(int i=0; i < n; i++){
        sum = sum + a[i];
    }
    avg = sum/ n;
    return avg;
}

int main(){
    float arr[100];
    int n = 100;
    for(int i=0;i<n/2;i++){
        arr[i] = 20;
    }
    for(int i=n/2;i<n;i++){
        arr[i] = 30.8;
    }
    print_float(arr[0]);
    print_char(10);
    float av = avg(arr, n);
    print_float(av);
    return 0;
}