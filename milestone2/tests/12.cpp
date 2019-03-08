class employee
{
  public:
    int salary;
};
class developer : public class employee
{
    class employee e;

  public:
    void salary()
    {
        cout << "Enter employee salary: ";
        cin >> e.salary; // access base class data member
        cout << "Employee salary: " << e.salary;
    }
};

class sum
{
    // hidden data from outside world
  private:
    int a, b, c;

  public:
    void add()
    {
        clrscr();
        cout << "Enter any two numbers: ";
        cin >> a >> b;
        c = a + b;
        cout << "Sum: " << c;
    }
};

class sum
{
  private:
    int a, b, c;

  public:
    void add()
    {
        clrscr();
        cout << "Enter any two numbers: ";
        cin >> a >> b;
        c = a + b;
        cout << "Sum: " << c;
    }
};

class Base
{
  public:
    void show()
    {
        cout << "Base class";
    }
};
class Derived : public class Base
{
  public:
    void show()
    {
        cout << "Derived Class";
    }
};

typedef class Derived* D_PTR;

void main()
{
    clrscr();
    class developer obj;
    obj.salary();
    getch();
    class Base b;    //Base class object
    class Derived d; //Derived class object
    b.show();        //Early Binding Ocuurs
    d.show();
    getch();
    class sum s;
    type  D_PTR A = as;
    s.add();
    getch();
}
