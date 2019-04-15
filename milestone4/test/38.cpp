class a{
  char b;
  int c[10];
};

int main(){
  int x(int* t){
    int *z=t;
    *z=5;
    return 4;
  }
  int t;
  x(&t);
  print_int(t);

  return 0;
}