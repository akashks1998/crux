class a{
  char b;
  int c[10];
};

int main(){
  int x(int* t){
    *t=8;
    return 4;
  }
  int t;
  x(&t);
  print_int(t);

  return 0;
}