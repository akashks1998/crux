
class A
{
  public:
    virtual void show()
    {
      cout << "Hello base class";
    }
};

class B : public A
{
  public:
    void show()
    {
      cout << "Hello derive class";
    }
};

void main()
{
  clrsct();
  A aobj;
  B bobj;
  A *bptr;
  bptr = &aobj;
  bptr->show(); // call base class function

  bptr = &bobj;
  bptr->show(); // call derive class function
  getch();
}
