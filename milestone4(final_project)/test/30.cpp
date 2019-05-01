// checking multi dim array
class a{
    int b;
};
int f(int x){
    return x;

}
int f(class a c){
    return c.b;
}


int main(){
    print_int(f(1));
    class a x;
    x.b=2;
    print_int(f(x));
    return 0;
}
