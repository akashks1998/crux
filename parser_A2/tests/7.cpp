void main()
{
int a, b, c, large;
clrscr();
cout<<"Enter any three number: ";
cin>>a>>b>>c;
large=a>b ? (a>c?a:c) : (b>c?b:c);
cout<<"Largest Number is: "<<large;
getch();
}
