
class A
{
  public:
    virtual void show()
    {
      cout << "Hello base class";
    }
};

class B : public class A
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
  type A aobj;
  class B bobj;
  class  A *bptr;
  bptr = &aobj;
  bptr->show(); // call base class function

  bptr = &bobj;
  bptr->show(); // call derive class function
  getch();
}
