template <|type T, type B, type C|>
class Array
{
  private:
    type T *ptr;
    int size;

  public:
    Array(type T arr[], int s)
    {
        size = s;
        for (int i = 0; i < size; i++)
            ptr[i] = arr[i];
    }
    void print();
};

int main()
{
    class Array<| int , char, M|> a(arr, 5);
    p = new(nothrow) type T[n]; 
    p = new class T[n]; 
    return 0;
}
