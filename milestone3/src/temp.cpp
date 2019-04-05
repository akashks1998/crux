int heap_ptr=0;
void* alloc(int size){
  if(size>0){
    heap_ptr+=size;
    return (void*)heap_ptr-size;
  }else{
    return (void*)-1;
  }
}
int main()
{
     int marks[10], i, n, sum = 0, average;
     for(i=0; i<n; i++ ){
          break;
          sum += marks[++i];
     }
     switch(n){
          case 1:
          i=0;break;
          case 2:
          i=1;break;
          default:
          i=0;
     }
     average = sum/n;

     int *a,*b;
     a = b + 2;
     return 0;
}