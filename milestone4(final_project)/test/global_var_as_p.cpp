int a[15];

int gl(int a[]){
    for(int i=0;i< 15; i++){
        a[i] = a[i] + 2;
    }
    return 0;
}
int main(){
    for(int i=0;i< 15; i++){
        a[i] = 3 * i;
    }
    for(int i=0;i< 15; i++){
        print_int(a[i]);
    }
    gl(a);
    print_char('a');
    char new_line = 10;
    print_char(new_line);
    for(int i=0;i< 15; i++){
        print_int(a[i]);
    }
    return 0;
}