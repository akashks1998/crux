class employee
{
  private:
    void sal();
};

void sal()
{
    int salary = 4000;
    cout << "Salary: " << salary;
}

void min()
{
    int fact(int);
    int i, f, num;
    clrscr();
    cout << "Enter any number: ";
    cin >> num;
    f = fact(num);
    cout << "Factorial: " << f;
    getch();
}

int fact(int n)
{
    if (a < 0)
        return (-1);
    if (a == 0)
        return (1);
    else
    {
        return (n * fact(n - 1));
    }
}

void main()
{
    class employee e;
    sal();
    getch();
}
