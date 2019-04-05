int heap_ptr=0;
void* alloc(int size){
  if(size>0){
    heap_ptr+=size;
    return (void*)heap_ptr-size;
  }else{
    return (void*)-1;
  }
}