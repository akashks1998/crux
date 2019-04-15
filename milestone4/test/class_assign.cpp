class dog{
    int a;
    int b[2];
    char c[2];
};
int kutta(class dog tommy ){
    print_int(tommy.a);
    tommy.b[1] = 1000;
    print_int(tommy.b[1]);
    print_char(tommy.c[1]);
    return 0;
}
int main(){
    class dog tommy;
    tommy.a = 500006;
    tommy.b[1] = 47363346;
    tommy.c[1] = 'c';
    kutta(tommy);
    print_int(tommy.b[1]);
    
    return 0;
}