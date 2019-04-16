int odd(int x);
int even(int n){
    if(n==0){
        return 1;
    }else{
        return odd(n-1);
    }
}
int odd(int n){
    if(n==0){
        return 0;
    }else{
        return even(n-1);
    }
}
int main(){
    print_int(even(5));
    return 0;
}