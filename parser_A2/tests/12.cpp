class employee
{
  public:
    int salary;
};
class developer : public employee
{
    employee e;

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
class Derived : public Base
{
  public:
    void show()
    {
        cout << "Derived Class";
    }
}

void
main()
{
    clrscr();
    developer obj;
    obj.salary();
    getch();
    Base b;    //Base class object
    Derived d; //Derived class object
    b.show();  //Early Binding Ocuurs
    d.show();
    getch();
    sum s;
    s.add();
    getch();
}
