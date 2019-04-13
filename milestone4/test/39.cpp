int a(int b[10],int c, float d){
  float e,f=0;
  if(f==0.0 && (c==0|| b[0]>=1 ) ){
    e=1.0;
    int k=(b[c]++);
    return k;
  }else{
    if(c<10){
      for(int i=0;i<c;i++){
        while(i<c-1){
          i++;
          b[i]=(i>>2);
          c=c|c;
          if(i==5){
            break;
          }else{
            continue;
          }
          return -1;
        }
      }
    }
  }
  return b[0];
}
int main(){
  int b[10],c=9,k;
   k=sizeof(int);
  float d=1.0;
  switch(k){
    case 1:
    d=2.0;
    break;
  }
  b[0]=100;
  int z=a(b,c,d);
  return 0;
}