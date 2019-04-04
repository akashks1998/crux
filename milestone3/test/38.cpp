int heap_ptr=0;
void* alloc(int size){
  if(size>0){
    heap_ptr+=size;
    return (void*)heap_ptr-size;
  }else{
    return (void*)-1;
  }
}
int main(){
  int size;
  int* a=new(int)[5];
  return 0;
}