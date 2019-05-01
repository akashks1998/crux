int main(){
    int f  = 100;
    int g = 300;
    int h = 12;
    int ret = 56;
    ret = ( ( (((f * g * h) + 3 ) / ret ) - 30 ) % 400 ) + ( (((f * g / h) - 90 ) / ret ) /45);
    print_int(ret);
    
    int p =0;
    p++;
    print_int(p);
    return 0;
}