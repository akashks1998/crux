template <|type T, type B, type C|>
class Array
{
  private:
    type T *ptr;
    int size;

  public:
    void Array(type T arr[], int s)
    {
        size = s;
        for (int i = 0; i < size; i++)
            ptr[i] = arr[i];
    }
    void print();
};

int main()
{
    class Array<| int , char, type M|> a(arr, 5);
    p = new type T[n]; 
    p = new class T[n]; 
    return 0;
}
