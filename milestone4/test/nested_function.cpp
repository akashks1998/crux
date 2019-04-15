
int x(int* t ){
  *t=6;
  return 0;
}
int a(int b){
  int x(int z){
    return z*z;
  }
  return x(b);
}
int main(){
  int z,*l;
  l=&z;
  x(l);
  print_int(z);
  int x(int* t){
    int *z=t;
    scan_int(*z);
    return 4;
  }
  int t;
  x(&t);
  print_int(a(t));
  print_int(t);

  return 0;
}