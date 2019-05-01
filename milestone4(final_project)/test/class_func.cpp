class hi{
    int j;
    int a[10];
    char c[8];
};

class hi :: int set_char(int c, char d){
    for(int i=0; i< 8; i++){
        this->a[i] = c++;
        this->c[i] = d++;
    }
    return 0;
}

int main(){
    class hi H;
    H.set_char(10,'a');
    for(int i=0; i< 8; i++){
        print_int(H.a[i]);
        print_char(H.c[i]);
    }

    return 0;
}