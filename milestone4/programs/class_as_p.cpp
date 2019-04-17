class hi{
    int a;
    int b;
};

int print_a(class hi h){
    h.b = 65;
    print_int(h.a);
    return 0;
}
int main(){
    class hi m;
    m.a = 40;
    m.b = 100;
    print_a(m);
    print_int(m.b);
  
    return 0;
}

