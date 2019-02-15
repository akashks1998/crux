template <|class T, B, C|>
class Array
{
  private:
    T *ptr;
    int size;

  public:
    Array(T arr[], int s)
    {
        ptr = new T[s];
        size = s;
        for (int i = 0; i < size; i++)
            ptr[i] = arr[i];
    }
    void print();
};

int main()
{
    Array<| int , char, M|> a(arr, 5);
    return 0;
}
