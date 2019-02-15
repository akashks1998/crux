

template <|typename T|> 
class Array { 
private: 
    T *ptr; 
    int size; 
public: 
    Array(T arr[], int s); 
    void print(); 
}; 
  

int main(){
    bubbleSort<|int,char,double|> a;
    return 1;
}