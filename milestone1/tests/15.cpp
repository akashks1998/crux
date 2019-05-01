
void abc()
{
    int i;
    cout << "data in abc:";
    cout << "Total no. of arguments: ", _argc;
    for (i = 0; i < _argc; i++)
    {
        cout << i + 1 << endl
             << "argument:" << _argv[i];
    }
}
void main(int argc, char *argv[])
{
    int i;
    clrscr();
    cout << "\n data in main:";
    cout << "\n total no. of arguments: " << argc;
    for (i = 0; i < argc; i++)
    {
        cout << i + 1 << endl
             << "arguments: " << argv[i];
    }
    abc();
    getch();
}
