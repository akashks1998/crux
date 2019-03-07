class Addition
{
  public:
    void sum(int a, int b)
    {
        cout << a + b;
    }
    void sum(int a, int b, int c)
    {
        cout << a + b + c;
    }
};
void main()
{   
    class Addition
    {
    public:
        void sum(int a, int b)
        {
            cout << a + b;
        }
        void sum(int a, int b, int c)
        {
            cout << a + b + c;
        }
    };
    clrscr();
    class Addition obj;
    obj.sum(10, 20);
    cout << endl;
    obj.sum(10, 20, 30);
}
