class a{
  char b;
  int c[10];
};

int main(){
  
  int* p=new(int)[10];
  for(int i=0;i<10;i++){
    p[i]=i*2;
    print_int(p[i]);
  }
  delete [] p;
  
  return 0;
}